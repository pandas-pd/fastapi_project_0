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
            return {"message" : f"invalid or duplicat username was given: {body.username}"}

        if (Validator.e_mail(body.e_mail) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid  or duplicat e-mail adress given: {body.e_mail}"}

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

    @staticmethod
    def role(body, response):

        #validation
        if (Validator.user(body.key_user) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid user key was given: {body.key_user}"}

        if (Validator.user_role(body.key_role) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid role key was given: {body.key_role}"}

        #key hanlidng
        ur_key      = DB.generate_model_key(model = User_roles)
        fk_us       = Key_to_id.users(key = body.key_user)
        fk_ro       = Key_to_id.role(key = body.key_role)

        #writing entry
        new_ur = User_roles(
            fk_ro               = fk_ro,
            fk_us               = fk_us,
            key                 = ur_key,
            timestamp           = int(time.time())
        )

        session.add(new_ur)
        session.commit()

        message : dict = {"message" : ur_key}
        return message


class Read():

    @staticmethod
    def user():

        #query
        query = select(
            Users.key,
            Users.username,
            Users.e_mail,
            Users.comment,
            Users.timestamp,
        ).select_from(Users)

        content = session.execute(query).fetchall()

        #format data
        response : list = []
        for row in content:

            item : dict = {
                "key"           : row[0],
                "username"      : row[1],
                "e_mail"        : row[2],
                "comment"       : row[3],
                "timestamp"     : row[4],
            }
            response.append(item)

        return response


class Update():

    @staticmethod
    def user(body, response):

        #validate inputs
        if (Validator.user(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return{"message" : f"invalid user_key was given: {body.key}"}

        if (Validator.username(username = body.username, initial = False, key_user = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid or duplicat username was given: {body.username}"}

        if (Validator.e_mail(e_mail = body.e_mail) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid or duplicat e_mail was given {body.e_mail}"}

        #query update
        query = session.query(Users).filter(Users.key == body.key).update({
            Users.username              : body.username,
            Users.e_mail                : body.e_mail,
            Users.comment               : body.comment,
            Users.timestamp             : int(time.time()),
        })
        session.commit()

        #reponse
        message : dict = {"message" : f"update user entry with key: {body.key}"}
        return message


class Delete():

    @staticmethod
    def user(body, response):

        #validate inputs
        if (Validator.user(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return{"message" : f"invalid user_key was given: {body.key}"}

        #delete roles bond to User
        id_us = Key_to_id.users(key = body.key)
        query = session.query(User_roles).filter(User_roles.fk_us == id_us).delete()
        session.commit(query)

        #delete user
        query = session.query(Users).filter(Users.key == body.key).delete()
        session.commit(query)

        message : dict = {"message" : f"deleted user and realted role entries with user key: {body.key}"}
        return message


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

    @staticmethod
    def reset_password():
        pass

    def change_password():
        pass
