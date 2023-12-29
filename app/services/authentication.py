from fastapi import status
from sqlalchemy import select

from db.base import session
from db.models.users import Users, User_roles

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

        #fetch user key and role to create jwt
        query = select(
            Users.key,
            User_roles.key,
        ).select_from(Users
        ).join(User_roles, User_roles.user, isouter = True
        ).filter(Users.username == body.username)

        content = session.execute(query).fetchall()

        key_user : int = None
        key_roles : list = []

        for row in content:
            key_user = int(row[0])
            key_roles.append(int(row[1]))

        #create and return jwt
        jwt = JWT_handler.issue_jwt(key_user = key_user, key_roles = key_roles)
        message : dict = {"access_token": jwt, "token_type": "bearer"}

        return message


    @staticmethod
    def logout(body, response):
        pass

    @staticmethod
    def check_permission():
        pass