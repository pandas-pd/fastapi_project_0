from db.base import session
from sqlalchemy import select, insert, delete, update

from db.models.enums import Skill_level, Project_status, User_role
from db.models.skills import Programming_languages, Libraries
from db.models.projects import Projects
from db.models.users import Users, User_roles

import random

class Validator():

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
    def sequence_number(number : int) -> bool:
        """validates order number, can be in range [1, n+1])"""

        if (number == None) or (number > 0):
            return True

        else:
            return False

    @staticmethod
    def project(key : int) -> bool:

        query       = select(Projects.key).select_from(Projects).where(Projects.key == key)
        conten      = session.execute(query).fetchone()

        if conten == None:
            return False
        else:
            return True

    @staticmethod
    def username(username : str) -> bool:

        query       = select(Users.username).select_from(Users).filter(Users.username == username)
        content     = session.execute(query).fetchall()

        if len(content) == 0:
            return True
        else:
            return False

    @staticmethod
    def e_mail(e_mail : str) -> bool:
        
        if e_mail == None:
            return True

        at_index : int      = e_mail.find("@")

        if at_index == -1:
            return False

        domain : str        = e_mail[at_index :]
        dot_index : int     = domain.find(".")

        if (dot_index == -1) or (dot_index == 1):
            return False

        else:
            return True


class Key_to_id():

    @staticmethod
    def skill_level(key : int) -> int:

        query = select(Skill_level.id_sl).select_from(Skill_level).where(Skill_level.key == key)
        content = session.execute(query).fetchone()

        id = int(content[0])
        return id

    @staticmethod
    def programming_languages(key : int) -> int:

        query = select(Programming_languages.id_pl).select_from(Programming_languages).where(Programming_languages.key == key)
        content = session.execute(query).fetchone()

        id = int(content[0])
        return id

    @staticmethod
    def libraries(key : int) -> int:

        query = select(Libraries.id_lb).select_from(Libraries).where(Libraries).where(Libraries.key == key)
        content = session.execute(query).fetchone()

        id = int(content[0])
        return id

    @staticmethod
    def project_status(key : int) -> int:

        query = select(Project_status.id_ps).select_from(Project_status).where(Project_status.key == key)
        content = session.execute(query).fetchone()

        id = int(content[0])
        return id


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