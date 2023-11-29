from db.base import session
from sqlalchemy import select, insert, delete, update
from db.models.enums import Skill_level, Project_status

class Read():

    @staticmethod
    def skill_level() -> dict:

        #define query
        query = select(Skill_level.key, Skill_level.value,).select_from(Skill_level)

        #fetch data
        result : object     = session.execute(query)
        content : list      = result.fetchall()

        #format data
        response : dict     = {}
        for row in content:
            response[int(row[0])] = str(row[1])

        return response

    @staticmethod
    def project_status() -> dict:

        #define query
        query = select(Project_status.key, Project_status.value).select_from(Project_status)

        #fetch data
        result : object     = session.execute(query)
        content : list      = result.fetchall()

        #format data
        response : dict = {}
        for row in content:
            response[int(row[0])] = str(row[1])

        return response