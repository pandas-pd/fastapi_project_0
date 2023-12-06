#import for automation and ease of use
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#import database url
from app.settings import DATABASE_URL

#import base for session handling
from app.db import base
from app.db.base import enums

class Controller():

    @staticmethod
    def main():

        #add new models here
        enum_models : list = [
            enums.Skill_level,
            enums.Project_status,
            enums.User_role,
        ]

        for model in enum_models:
            Controller.empty_enum(model = model)

        Controller.fill_enum()

        return

    @staticmethod
    def empty_enum(model):

        base.session.query(model).delete()
        base.session.commit()

        return

    def fill_enum():

        #add populating functions here
        Data.skill_level()
        Data.project_status()
        Data.user_role()

class Data():

    @staticmethod
    def skill_level():

        #declare data
        objects : dict = [
            enums.Skill_level(key = 0,       value = "undefined"),
            enums.Skill_level(key = 1,       value = "novice"),
            enums.Skill_level(key = 2,       value = "competent"),
            enums.Skill_level(key = 3,       value = "advanced"),
            enums.Skill_level(key = 4,       value = "proficient"),
            enums.Skill_level(key = 5,       value = "expert"),
        ]

        #write to database
        base.session.bulk_save_objects(objects)
        base.session.commit()

        print("skill_level enum populated")
        return

    @staticmethod
    def project_status():

        #declare data
        objects : dict = [
            enums.Project_status(key = 0,       value = "undefined"),
            enums.Project_status(key = 1,       value = "idea"),
            enums.Project_status(key = 2,       value = "concept"),
            enums.Project_status(key = 3,       value = "in progress"),
            enums.Project_status(key = 4,       value = "done"),
            enums.Project_status(key = 5,       value = "cancelled"),
        ]

        #write to database
        base.session.bulk_save_objects(objects)
        base.session.commit()

        print("project_status enum populated")
        return

    @staticmethod
    def user_role():

        #declate data
        objects : dict = [
            enums.User_role(key = 0,        value = "admin"),
            enums.User_role(key = 1,        value = "guest"),
        ]

        #write to database
        base.session.bulk_save_objects(objects)
        base.session.commit()

        print("role enum populated")
        return



if __name__ == "__main__":
    Controller.main()