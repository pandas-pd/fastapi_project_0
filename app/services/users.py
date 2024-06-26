from db.base import session
from sqlalchemy import select, insert, delete, update
from fastapi import status
import time

from db.models.users import Users, User_roles
from db.models.enums import User_role

from services.helper_general import *
from services.helper_password import Password_handler
from services.helper_email import E_mail


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

        if (Validator.user_roles_duplicates(key_user = body.key_user, key_role = body.key_role) == False):
            response.status_code = status.HTTP_409_CONFLICT
            return {"message" : f"role already exists for given user, role : {body.key_role}, user : {body.key_user}"}

        #key hanlidng
        ur_key      = DB.generate_model_key(model = User_roles)
        fk_us       = Key_to_id.users(key = body.key_user)
        fk_ro       = Key_to_id.role(key = body.key_role)

        #writing entry
        new_ur = User_roles(
            fk_ro               = fk_ro,
            fk_us               = fk_us,
            key                 = ur_key,
            comment             = body.comment,
            timestamp           = int(time.time())
        )

        session.add(new_ur)
        session.commit()

        message : dict = {"message" : ur_key}
        return message

    @staticmethod
    def validate_username(body, response):

        if (Validator.username(body.username) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : "username is invalid or already exists"}

        else:
            response.status_code = status.HTTP_200_OK
            return {"message" : "username is valid and available"}


class Read():

    @staticmethod
    def all_users():

        #query
        query_users = select(
            Users.key,
            Users.username,
            Users.e_mail,
            Users.comment,
            Users.timestamp,
        ).select_from(Users)

        content_users = session.execute(query_users).fetchall()

        #format data
        response : list = []
        for row in content_users:

            roles : list = Read.roles(key_user = row[0]) #not the best way to handle this but it works

            item : dict = {
                "key"           : row[0],
                "username"      : row[1],
                "e_mail"        : row[2],
                "comment"       : row[3],
                "timestamp"     : row[4],
                "roles"         : roles,
            }

            response.append(item)

        return response

    @staticmethod
    def user(key_user : int):

        #query
        query = select(
            Users.key,
            Users.username,
            Users.e_mail,
            Users.comment,
            Users.timestamp,
        ).select_from(Users
        ).filter(Users.key == key_user)

        content = session.execute(query).fetchone()
        roles = Read.roles(key_user = key_user)

        response : dict = {
            "key"           : content[0],
            "username"      : content[1],
            "e_mail"        : content[2],
            "comment"       : content[3],
            "timestamp"     : content[4],
            "roles"         : roles,
        }

        return response


    @staticmethod
    def roles(key_user : int, response : object = None):

        #validait key
        if (Validator.user(key = key_user) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid user key was given: {key_user}"}

        #qurey data
        query = select(
            User_roles.key,
            User_role.key,
            User_roles.timestamp,
        ).select_from(User_roles
        ).join(User_role, User_roles.role
        ).join(Users, User_roles.user
        ).filter(Users.key == key_user)

        content = session.execute(query).fetchall()

        #format data
        response : list = []

        for row in content:

            response.append({
                "key_user_role"             : row[0],
                "role"                      : row[1],
                "timestamp"                 : row[2],
            })

        return response


class Update():

    @staticmethod
    def user(body, response):

        #validate inputs
        if (Validator.user(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid user_key was given: {body.key}"}

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

    @staticmethod
    def password(body, response):

        #validation inputs
        if (Validator.user(key = body.key_user) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid user_key was given: {body.key_user}"}

        if (Password_handler.password_match(password = body.password_old, user_key = body.key_user) == False):
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return {"message" : f"invalid password was provided"}

        #create new password hash and salt
        salt, hashed_password = Password_handler.salt_and_hash(body.password_new)

        query = session.query(Users).filter(Users.key == body.key_user).update({
            Users.password_hash         : hashed_password,
            Users.salt                  : salt,
            Users.comment               : body.comment,
            Users.timestamp             : int(time.time()),
        })

        session.commit()

        #respons
        message : dict = {"message" : f"updated password for user with key: {body.key_user}"}
        return message

    @staticmethod
    def reset_password(body, response):

        if (Validator.username_on_existing(body.username) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid username was provided: {body.username}"}

        #fetch user key (clumsy but works)
        query   = select(Users.id_us, Users.e_mail).select_from(Users).filter(Users.username == body.username)

        content                 = session.execute(query).fetchone()
        id_us                   = content[0]
        e_mail                  = content[1]

        password : str          = Password_handler.generate_password(length = 6)
        salt, password_hash     = Password_handler.salt_and_hash(password)

        #save new password
        query = session.query(Users).filter(Users.id_us == id_us).update({
            Users.password_hash             : password_hash,
            Users.salt                      : salt,
            Users.comment                   : "password reset",
            Users.timestamp                 : int(time.time()),
        })
        session.commit()

        #send new password to user
        E_mail.message(to = e_mail, subject = "password reset", body = f"Password was reset for user {body.username}. Your new initial password is:\n{password}")

        message : dict = {"message" : "password reset successfull"}
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
        session.commit()

        #delete user
        query = session.query(Users).filter(Users.key == body.key).delete()
        session.commit()

        message : dict = {"message" : f"deleted user and realted role entries with user key: {body.key}"}
        return message

    @staticmethod
    def role(body, response):

        #validate inputs
        if (Validator.user_roles(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid role_key was goven: {body.key}"}

        #delete roles entry
        query = session.query(User_roles).filter(User_roles.key == body.key).delete()
        session.commit()

        message : dict = {"message" : f"delted user role and with role key: {body.key}"}
        return message
