from db.base import session
from sqlalchemy import select, insert, delete, update

from db.models.enums import Skill_level, Project_status
from db.models.skills import Programming_languages, Libraries
from db.models.projects import Projects

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

        #fetch empty data
        if number == None:
            return True

        #fetch data and order it
        query           = select(Projects.sequence_number).select_from(Projects).where(Projects.sequence_number != None)
        conten          = session.execute(query).fetchall()
        sequence        = [row[0] for row in conten]

        sequence.sort()

        #validate order number (can be in range [0, n+1]). rearanging is done in separate funciton
        if (len(sequence) == 0) and (number == 1):
            return True

        elif (len(sequence) > 0) and ( (number in sequence) or (number - 1 == sequence[-1])):
            return True

        else:
            return False


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