from db.base import session
from sqlalchemy import select, insert, delete, update
from fastapi import status
import time

import bcrypt

from db.models.users import Users, User_roles
from db.models.enums import User_role

from settings import ENCODING, SALT_ROUNDS

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

        #generate key, password salt and password hash
        salt, hashed_password       = Password_handler.salt_and_hash(body.password)
        us_key : int                = DB.generate_model_key(model = Users)

        new_us = Users(
            username        = body.username,
            e_mail          = body.e_mail,
            salt            = salt,
            password_hash   = hashed_password,
            comment         = body.comment,
            key             = us_key,
            timestamp       = int(time.time())
        )

        session.add(new_us)
        session.commit()

        message : dict = {"message" : us_key}
        return message


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


class Password_handler():

    @staticmethod
    def salt_and_hash(password : str) -> str:

        #generate salt and hash
        salt : bytes                    = bcrypt.gensalt(rounds = SALT_ROUNDS)
        hashed_password : bytes         = bcrypt.hashpw(password.encode(ENCODING), salt)

        #endcoding for explicity
        s_salt : str                    = salt.decode(ENCODING)
        s_hashed_password : str         = hashed_password.decode(ENCODING)

        return s_salt, s_hashed_password

    @staticmethod
    def password_match(username : str, password : str) -> bool:

        #password_match : bool = bcrypt.checkpw(password_input.encode(encoding), stored_hashed_password.encode(encoding))
        pass
