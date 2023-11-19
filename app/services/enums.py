from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level

class Read():

    @staticmethod
    def skill_level():

        #define query
        query = select(
            Skill_level.key, Skill_level.value,
        ).select_from(
            Skill_level
        )

        #fetch data
        result : object     = session.execute(query)
        content : list      = result.fetchall()

        #format data
        response : dict     = {}
        for row in content:
            response[int(row[0])] = str(row[1])

        return response