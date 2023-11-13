from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level
from services.formater import sqlalchemy_to_dict

class Read():

    def skill_level():

        query = select(
            Skill_level.code,
            Skill_level.value,
        ).select_from(
            Skill_level
        )

        content = session.execute(query).fetchall()
        print(content)
        #content = sqlalchemy_to_dict(content)

        return {"content": 0}