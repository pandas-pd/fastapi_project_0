from db.base import session
from sqlalchemy import select, insert, delete, update, and_, func
from fastapi import status
import time

from db.models.projects import Projects
from db.models.enums import Project_status

from services.helper import *

class Write():

    @staticmethod
    def project(body, response):

        #validation
        if (Validator.project_status(key = body.key_project_status) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid project status key was given: {body.key_project_status}"}

        if (Validator.sequence_number(number = body.sequence_number) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid sequence number was given: {body.sequence_number}"}

        #udpate existing sequence numbers and inserting new entry
        if body.sequence_number != None:
            sequence_number : int = Sequence_logic.adjust_payload_sequence_number(body.sequence_number)
            Sequence_logic.sequence_update_on_insert(tbi_sequence_number = sequence_number)
        else:
            sequence_number = None

        #generate keys and insert data
        pr_key = DB.generate_model_key(Projects)
        fk_ps = Key_to_id.project_status(body.key_project_status)

        new_pr = Projects(
            fk_ps           = fk_ps,
            key             = pr_key,
            name            = body.name,
            description     = body.description,
            sequence_number = sequence_number,
            link            = body.link,
            timestamp       = int(time.time()),
        )

        session.add(new_pr)
        session.commit()

        message : dict = {"message" : pr_key}

        return message


class Read():

    @staticmethod
    def project():

        query = select(
            Projects.key,
            Projects.name,
            Projects.description,
            Projects.sequence_number,
            Projects.link,
            Project_status.key,
            Projects.timestamp,
        ).select_from(Projects
        ).join(Project_status, isouter = True)

        conten = session.execute(query).fetchall()

        #format data
        response : list = []
        for row in conten:

            item : dict = {
                "key"               : row[0],
                "name"              : row[1],
                "description"       : row[2],
                "sequence_number"   : row[3],
                "link"              : row[4],
                "project_status"    : row[5],
                "timestamp"         : row[6],
            }
            response.append(item)

        return response


class Udpdate():

    @staticmethod
    def project(body, response):

        #validate key
        if (Validator.project_key(body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid project key was given: {body.key}"}

        if (Validator.project_status(body.key_project_status) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid project status key was given: {body.key_project_status}"}

        if (Validator.sequence_number(body.sequence_number) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid project status key was given: {body.key_project_status}"}

        #update exisitng sequence numbers if needed
        if (body.sequence_number != None):
            sequence_number : int = Sequence_logic.adjust_payload_sequence_number(sequence_number = body.sequence_number, insert = False)
        else:
            sequence_number = None

        Sequence_logic.sequence_update_on_update(new_sequence_number = sequence_number, key = body.key) #applies the sequence shift for entry to be updated

        #translate keys
        fk_ps = Key_to_id.project_status(key = body.key_project_status)

        #update db entry
        session.query(Projects).filter(Projects.key == body.key).update({
            Projects.fk_ps              : fk_ps,
            Projects.name               : body.name,
            Projects.description        : body.description,
            Projects.sequence_number    : sequence_number,
            Projects.link               : body.link,
            Projects.timestamp          : int(time.time())
        })

        return {"message" : f"update project entry with key: {body.key}"}

class Delete():

    @staticmethod
    def project(body, response):
        pass

class Sequence_logic():

    @staticmethod
    def sequence_update_on_insert(tbi_sequence_number : int) -> None:
        """shifts the sequence number of the projects table when inserting an entry"""

        #update sequence numbers to keep everything in odrer
        session.query(Projects).filter(and_(
            Projects.sequence_number != None,
            Projects.sequence_number >= tbi_sequence_number,
        )).update(
            {Projects.sequence_number : Projects.sequence_number + 1}
        )
        session.commit()

        return

    @staticmethod
    def sequence_update_on_update(new_sequence_number, key : int) -> None:
        """shifts the sequence number of the projects table when updateing an entry"""

        #fetch old seucence number
        query                       = select(Projects.sequence_number).select_from(Projects).filter(Projects.key == key)
        content                     = session.execute(query).fetchone()
        old_sequence_number         = content[0] #can be int or None

        if (old_sequence_number == None) and (new_sequence_number == None):
            return

        elif (old_sequence_number == None) and (new_sequence_number != None):

            session.query(Projects).filter(Projects.sequence_number >= new_sequence_number
            ).update({Projects.sequence_number : Projects.sequence_number + 1})
            session.commit()

        elif (old_sequence_number != None) and (new_sequence_number == None):

            #shift all else -1, according to old sequence number
            session.query(Projects).filter(Projects.sequence_number > old_sequence_number
            ).update({Projects.sequence_number : Projects.sequence_number - 1})
            session.commit()

        #case both not None
        elif (old_sequence_number < new_sequence_number): # case 1

            #apply shift for all needed number to -1, expect entry to be updated
            session.query(Projects).filter(and_(
                Projects.sequence_number <= new_sequence_number,
                Projects.sequence_number > old_sequence_number,
                Projects.key != key) #extra precaution
            ).update({Projects.sequence_number : Projects.sequence_number -1})
            session.commit()

        elif (old_sequence_number > new_sequence_number): # case 2

            #apply shift for all needed number to +1, expect entry to be updated
            session.query(Projects).filter(and_(
                Projects.sequence_number >= new_sequence_number,
                Projects.sequence_number < old_sequence_number,
                Projects.key != key)
            ).update({Projects.sequence_number : Projects.sequence_number +1})
            session.commit()

        session.query(Projects).filter(Projects.key == key).update({Projects.sequence_number : new_sequence_number})
        session.commit()

        return

    @staticmethod
    def sequence_update_on_delete(tbd_sequence_number : int) -> None:
        """shifts the sequence number of the projects table when deleting an entry"""
        pass

    @staticmethod
    def adjust_payload_sequence_number(sequence_number : int, insert : bool = True) -> int:
        """shift vlaues to max if needed"""

        #fetch data and order it
        query                           = select(func.max(Projects.sequence_number)).select_from(Projects)
        content                         = session.execute(query).fetchone()
        max_sequence_number : int       = content[0]

        #calculate new seq number for them to be in a row
        if (max_sequence_number == None):
            return 1

        elif (insert == True) and (sequence_number > max_sequence_number + 1):
            return max_sequence_number + 1

        elif (insert == False) and (sequence_number > max_sequence_number):
            return max_sequence_number

        else:
            return sequence_number