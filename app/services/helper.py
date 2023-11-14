from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level
from db.models.skills import Programming_languages
import random

class Validator():

    @staticmethod
    def skill_level(key : int) -> bool:

        #fetch data
        query       = select(Skill_level.key).select_from(Skill_level)
        content      = session.execute(query).fetchall()

        #create list with available codes
        keys : list         = []
        for row in content:
            keys.append(row[0])

        #check validity
        if (key in keys):
            return True
        else:
            return False

    @staticmethod
    def programming_language(key : int) -> bool:

        #fetch data
        query       = select(Programming_languages.key).select_from(Programming_languages)
        content     = session.execute(query).fetchall()

        #create list with availbale entries
        keys : list         = []
        for row in content:
            keys.append(row[0])

        if (key in keys):
            return True
        else:
            return False


class Generator():

    @staticmethod
    def model_key(model : object) -> int:

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