from db.base import session
from sqlalchemy import select, insert, delete, update, and_, func
from fastapi import status
import time

from db.models.projects import Projects
from db.models.enums import Project_status

from services.helper_general import *
from services.helper_project_sequence import *

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
        if (Validator.project(body.key) == False):
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

        session.commit()
        return {"message" : f"update project entry with key: {body.key}"}


class Delete():

    @staticmethod
    def project(body, response):

        #delete entry
        if (Validator.project(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid project key was given: {body.key}"}

        #handle sequence
        Sequence_logic.sequence_update_on_delete(key = body.key)

        session.query(Projects).filter(Projects.key == body.key).delete()
        session.commit()

        return {"message" : f"deleted libray entry with key: {body.key}"}
