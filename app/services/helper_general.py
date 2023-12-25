from db.base import session
from sqlalchemy import select, insert, delete, update

from db.models.enums import Skill_level, Project_status, User_role
from db.models.skills import Programming_languages, Libraries
from db.models.projects import Projects
from db.models.users import Users, User_roles

import random

class Validator():

    """todo: clean up this mess"""

    ### Generic, should be fixed

    @staticmethod
    def skill_level(key : int) -> bool:

        #fetch data
        query       = select(Skill_level.key).select_from(Skill_level).where(Skill_level.key == key)
        content      = session.execute(query).fetchone() #key is unique

        #validate key
        if content == None:
            return False
        else:
            return True

    @staticmethod
    def programming_language(key : int) -> bool:

        #fetch data
        query       = select(Programming_languages.key).select_from(Programming_languages).where(Programming_languages.key == key)
        content     = session.execute(query).fetchone() #key is unique

        #validate key
        if content == None:
            return False
        else:
            return True

    @staticmethod
    def library(key : int) -> bool:

        #fetch data
        query       = select(Libraries.key).select_from(Libraries).where(Libraries.key == key)
        content     = session.execute(query).fetchone() #key is unique

        if content == None:
            return False
        else:
            return True

    @staticmethod
    def project_status(key : int) -> bool:

        #fetch enum data
        query       = select(Project_status.key).select_from(Project_status).where(Project_status.key == key)
        conten      = session.execute(query).fetchone() #key is unique

        if conten == None:
            return False
        else:
            return True

    @staticmethod
    def project(key : int) -> bool:

        query       = select(Projects.key).select_from(Projects).where(Projects.key == key)
        conten      = session.execute(query).fetchone()

        if conten == None:
            return False
        else:
            return True

    @staticmethod
    def user_role(key : int) -> bool:

        query       = select(User_role.key).select_from(User_role).filter(User_role.key == key)
        content     = session.execute(query).fetchone()

        if content == None:
            return False
        else:
            return True

    @staticmethod
    def user_roles(key : int):

        query       = select(User_roles.key).select_from(User_roles).filter(User_roles == key)
        content     = session.execute(query).fetchall()

        if content == None:
            return False
        else:
            return True


    ### none general

    @staticmethod
    def sequence_number(number : int) -> bool:
        """validates order number, can be in range [1, n+1])"""

        if (number == None) or (number > 0):
            return True

        else:
            return False

    @staticmethod
    def username(username : str, initial : bool = True, key_user : int = None) -> bool:

        #forbidden charaters in user name like spaces
        forbidden_chars : list = ["&", "=", "'", ",", ".", "/", "\\", "@"]

        for char in username:
            if char in forbidden_chars:
                return False

        #check on update if old == new
        if initial == False:

            query       = select(Users.username).select_from(Users).filter(Users.key == key_user)
            content      = session.execute(query).fetchone() #is unuqie

            if (str(username) == str(content[0])):
                return True

        #checking for duplicates in datatbase if new entry
        query       = select(Users.username).select_from(Users).filter(Users.username == username)
        content     = session.execute(query).fetchall()

        if len(content) == 0:
            return True
        else:
            return False

    @staticmethod
    def e_mail(e_mail : str) -> bool:

        at_index : int      = e_mail.find("@")

        if at_index == -1:
            return False

        domain : str        = e_mail[at_index :]
        dot_index : int     = domain.find(".")

        if (dot_index == -1) or (dot_index == 1):
            return False

        else:
            return True

    @staticmethod
    def user(key : int = None) -> bool:

        if key == None:
            return True

        query       = select(Users.key).select_from(Users).filter(Users.key == key)
        content      = session.execute(query).fetchone()

        if content == None:
            return False
        else:
            return True

    @staticmethod
    def user_roles_duplicates(key_user : int, key_role):

        #fetch all roles for given user
        query = select(
            User_role.key,
        ).select_from(User_roles
        ).join(User_role, User_roles.role
        ).join(Users, User_roles.user
        ).filter(Users.key == key_user)

        content = session.execute(query).fetchall()

        #compile all available roles
        roles : list = [row[0] for row in content]

        if (key_role in roles):
            return False
        else:
            return True

    @staticmethod
    def username_on_reset(username : str):

        query       = select(Users.username).select_from(Users).filter(Users.username == username)
        content     = session.execute(query).fetchone()

        if content == None:
            return False
        else:
            return True

    @staticmethod
    def e_mail_on_reset(e_mail : str):
        """deprecated"""

        query       = select(Users.e_mail).select_from(Users).filter(Users.e_mail == e_mail)
        content     = session.execute(query).fetchone()

        if content == None:
            return False
        else:
            return True


class Key_to_id():

    """todo: clean up this mess"""

    def __handler(query):

        content = session.execute(query).fetchone()
        id = int(content[0])
        return id

    @staticmethod
    def skill_level(key : int) -> int:

        query = select(Skill_level.id_sl).select_from(Skill_level).filter(Skill_level.key == key)
        return int(Key_to_id.__handler(query))

    @staticmethod
    def programming_languages(key : int) -> int:

        query = select(Programming_languages.id_pl).select_from(Programming_languages).filter(Programming_languages.key == key)
        return int(Key_to_id.__handler(query))

    @staticmethod
    def libraries(key : int) -> int:

        query = select(Libraries.id_lb).select_from(Libraries).where(Libraries).filter(Libraries.key == key)
        return int(Key_to_id.__handler(query))

    @staticmethod
    def project_status(key : int) -> int:

        query = select(Project_status.id_ps).select_from(Project_status).filter(Project_status.key == key)
        return int(Key_to_id.__handler(query))

    @staticmethod
    def users(key : int) -> int:

        query = select(Users.id_us).select_from(Users).filter(Users.key == key)
        return int(Key_to_id.__handler(query))

    @staticmethod
    def role(key : int) -> int:

        query = select(User_role.id_ro).select_from(User_role).filter(User_role.key == key)
        return int(Key_to_id.__handler(query))

class DB():

    @staticmethod
    def generate_model_key(model : object) -> int:

        #fetch keys in model
        keys : list = []
        query       = select(model.key).select_from(model)
        content     = session.execute(query).fetchall()

        for row in content:
            keys.append(int(row[0]))

        #generate new key
        key = None
        while (key == None or key in keys):
            key = random.randint(100_000, 999_999)

        return key