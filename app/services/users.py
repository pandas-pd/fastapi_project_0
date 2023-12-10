from db.base import session
from sqlalchemy import select, insert, delete, update
from fastapi import status
import time

from db.models.users import Users, User_roles
from db.models.enums import User_role

from services.helper import *

class Write():

    @staticmethod
    def user(body, response):

        #validte username (must be unique)
        if (Validator.username(body.username) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"given username already exists: {body.username}"}

        if (Validator.e_mail(body.e_mail) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"given username already exists: {body.username}"}

        return


class Read():

    @staticmethod
    def user(body, response):
        pass



class Update():

    @staticmethod
    def user(body, response):
        pass



class Delete():

    @staticmethod
    def user(body, response):
        pass
