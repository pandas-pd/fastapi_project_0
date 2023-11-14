from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level
import random

class Validator():

    def skill_level(key : int) -> bool:

        #fetch data
        query       = select(Skill_level.key).select_from(Skill_level)
        result      = session.execute(query)
        content     = result.fetchall()

        #create list with available codes
        keys : list         = []
        list(map(
            lambda row: keys.append(row[0]),
            content
        ))

        #check validity
        if (key in keys):
            return True
        else:
            return False

class Generator():

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