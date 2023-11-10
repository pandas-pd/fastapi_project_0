#import for automation and ease of use
import inspect

#import base for session handling
from app.db import base

#import all enum models which need to be populated
from app.db.models.enums import Skill_level

class Controller():

    @staticmethod
    def main():

        #add new models here
        enum_models : list = [
            Skill_level,
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

class Data(object):

    def skill_level():

        #declare data
        objects : dict = [
            Skill_level(code = 0,       value = "undefined"),
            Skill_level(code = 1,       value = "novice"),
            Skill_level(code = 2,       value = "competent"),
            Skill_level(code = 3,       value = "advanced"),
            Skill_level(code = 4,       value = "proficient"),
            Skill_level(code = 5,       value = "expert"),
        ]

        #write to database
        base.session.bulk_save_objects(objects)
        base.session.commit()

        print("skill_level enum populated")
        return

if __name__ == "__main__":
    Controller.main()