from db.base import session
from sqlalchemy import select, insert, delete, update
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

        #generate keys
        pr_key = DB.generate_model_key(Projects)
        fk_ps = Key_to_id.project_status(body.key_project_status)

        #udpate existing sequence numbers
        if body.sequence_number != None:
            DB.update_project_sequence(tba_sequence_number = body.sequence_number)

        #continue here

        name : str
        description : str
        sequence_number : Optional[str]
        link : Optional[str]
        key_project_status : int


class Read():

    @staticmethod
    def project(body, response):
        pass

class Udpdate():

    @staticmethod
    def project(body, response):
        pass

class Delete():

    @staticmethod
    def project(body, response):
        pass