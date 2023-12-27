from fastapi import status
from sqlalchemy import select

from db.base import session
from db.models.users import Users

from services.helper_authentication import JWT_handler, Authentication
from services.helper_general import Validator
from services.helper_password import Password_handler


class Services():

    @staticmethod
    def login(body, response):

        #verify inputs
        if (Validator.username_on_existing(username = body.username) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid username was given: {body.username}"}

        if (Password_handler.password_match(password = body.password, username = body.username) == False):
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return {"message" : f"invalid password was provided"}

        #fetch user key to create jwt
        query               = select(Users.key).select_from(Users).filter(Users.username == body.username)
        us_key : int        = session.execute(query).fetchone()[0]

        #create jwt


    @staticmethod
    def logout(body, response):
        pass

    @staticmethod
    def check_permission():
        pass