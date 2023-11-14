from db.base import session
from sqlalchemy import select, insert, delete, update
from fastapi import status
import time

from db.models.skills import Programming_languages, Libraries
from db.models.enums import Skill_level

from services.helper import *

class Write():

    @staticmethod
    def programming_language(body, response):

        skill_level_valid : bool = Validator.skill_level(int(body.skill_level))

        #validate skill level
        if skill_level_valid is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was given: {body.skill_level}"}

        #generate key and
        pl_key = Generator.model_key(model = Programming_languages)
        print(pl_key)

        #write entry
        new_pl = Programming_languages(
            fk_sl       = body.skill_level,
            name        = body.name,
            comment     = body.comment,
            key         = pl_key,
            timestamp   = int(time.time()),
        )
        session.add(new_pl)
        session.commit()

        message = {"message" : pl_key}

        return message


class Read():

    @staticmethod
    def all_programming_languages():
        """reads all skill from the corresponing model withoug filters"""

        column_names = Programming_languages.__table__.columns.keys()

        query = select(
            Programming_languages.name,
            Programming_languages.comment,
            Programming_languages.timestamp,
            Skill_level.code,
            Skill_level.code,
        ).join_from(
            Programming_languages,
            Skill_level,
        )

        content = session.execute(query).fetchall()

        #to be formated
        response = {
            "cols" : column_names,
            "content" : content,
        }

        return response

class Update():
    pass

class Delete():
    pass
