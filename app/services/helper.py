from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level
from db.models.skills import Programming_languages, Libraries
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