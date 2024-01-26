from fastapi import status, HTTPException
from sqlalchemy import select

from db.base import session
from db.models.users import Users, User_roles
from db.models.enums import User_role

from services.helper_authentication import JWT_handler
from services.helper_general import Validator
from services.helper_password import Password_handler

from settings import JWT_NAME, JWT_SECURE, JWT_ACCESS_TOKEN_EXPIRE_SECONDS


class Services():

    @staticmethod
    def login(body, response):

        #verify inputs
        if (Validator.username_on_existing(username = body.username) == False):
            raise HTTPException(status_code=401,detail="Bad username or password")

        if (Password_handler.password_match(password = body.password, username = body.username) == False):
            raise HTTPException(status_code=401,detail="Bad username or password")

        #fetch user key and role to create jwt

        """
        query = select(
            Users.key,
            User_role.key,
        ).select_from(User_roles
        ).join(Users, User_roles.user, isouter = True
        ).join(User_role, User_roles.role, isouter = True
        ).filter(Users.username == body.username)
        """

        query = select(
            Users.key,
            User_role.key,
        ).select_from(Users
        ).outerjoin(User_roles, Users.id_us == User_roles.fk_us
        ).join(User_role, User_roles.role, isouter = True
        ).filter(Users.username == body.username)

        content = session.execute(query).fetchall()

        key_user : int = None
        key_roles : list = []

        for row in content:
            key_user = int(row[0])

            if (row[1] != None):
                key_roles.append(int(row[1]))

        #create and set
        jwt = JWT_handler.issue_jwt(key_user = key_user, key_roles = key_roles)

        response.set_cookie(
            key = JWT_NAME,
            value = jwt,
            secure = JWT_SECURE,
            max_age = JWT_ACCESS_TOKEN_EXPIRE_SECONDS,
        )

        return {"message" : "Login successful"}

    @staticmethod
    def logout(response):

        response.delete_cookie(key = JWT_NAME)
        return {"message" : "Logout successful"}

    @staticmethod
    def permission_handler(claims : dict, required_roles : list, user_dependent : bool = False, key_user : int = None) -> None:
        """if a request is user dependent, but an admin role is given and the admin role is possible, then admin can read the data anyway"""

        #check role requirements
        role_permission : bool = False

        for role in claims["roles"]:
            if (role in required_roles):
                role_permission = True

        if (role_permission == False):
            raise JWT_handler.credentials_exception

        #check user dependency
        if (user_dependent == True) and (int(claims["sub"]) != key_user):
                raise JWT_handler.credentials_exception

        return None