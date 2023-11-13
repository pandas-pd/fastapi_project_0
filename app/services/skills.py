from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.skills import Programming_languages, Libraries
from db.models.enums import Skill_level

class Write():
    pass

class Read():

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
