#import for automation and ease of use
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#import base for session handling
import base
from base import enums

class Controller():

    @staticmethod
    def main():

        #add new models here
        enum_models : list = [
            enums.Skill_level,
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

class Data():

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

if __name__ == "__main__":
    Controller.main()