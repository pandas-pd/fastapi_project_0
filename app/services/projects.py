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
            Sequence_logic.sequence_update_on_insert(tbi_sequence_number = body.sequence_number)
            sequence_number : int = Sequence_logic.adjust_payload_sequence_number(body.sequence_number)
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
        pass

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
    def sequence_update_on_update(tbu_sequence_number : int, key) -> None:
        """shifts the sequence number of the projects table when updateing an entry"""
        pass

    @staticmethod
    def sequence_update_on_delete(tbd_sequence_number : int) -> None:
        """shifts the sequence number of the projects table when deleting an entry"""
        pass

    @staticmethod
    def adjust_payload_sequence_number(sequence_number : int) -> int:
        """shift vlaues to max if needed"""

        #fetch data and order it
        query                           = select(func.max(Projects.sequence_number)).select_from(Projects)
        content                         = session.execute(query).fetchone()
        max_sequence_number : int       = content[0]

        #calculate new seq number for them to be in a row
        if (max_sequence_number == None):
            return 1
        elif (sequence_number > max_sequence_number + 1):
            return max_sequence_number + 1
        else:
            return sequence_number