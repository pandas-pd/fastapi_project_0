from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level

class Read():

    def skill_level():

        #define query
        query = select(
            Skill_level.code, Skill_level.value,
        ).select_from(
            Skill_level
        )

        #fetch data
        result : object     = session.execute(query)
        #header : tuple      = result.keys()
        content : list      = result.fetchall()

        #format data
        response : dict     = {}
        for row in content:
            response[int(row[0])] = str(row[1])

        return response