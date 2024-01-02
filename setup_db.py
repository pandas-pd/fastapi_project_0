#import for automation and ease of use
from sqlalchemy import create_engine, Column, Integer, String, insert, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import time
import bcrypt

#import database url
from app.settings import DATABASE_URL, ENCODING, SALT_ROUNDS

#import base for session handling
from app.db import base
from app.db.base import enums
from app.db.base import users

class Controller():

    default_admin_username : str = "admin"
    default_admin_password : str = "admin"

    @staticmethod
    def main():

        ui_setup_default_admin : str = input(f"""
            setup a default admin user with admin role?
            username:\t{Controller.default_admin_username}
            password:\t{Controller.default_admin_password}
            (y/n):\t""")

        # ENUMS

        #add new models here
        enum_models : list = [
            enums.Skill_level,
            enums.Project_status,
            enums.User_role,
        ]

        for model in enum_models:
            Controller.empty_enum(model = model)

        Controller.fill_enum()

        # DEFAULT ADMI user
        if (ui_setup_default_admin == "y"):
            Data.admin_user()

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

        return

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
            enums.User_role(key = 0,        value = "admin"), #if changed, look at the authenticaiton schema handler in services.authentication.permission_handler
            enums.User_role(key = 1,        value = "guest"),
        ]

        #write to database
        base.session.bulk_save_objects(objects)
        base.session.commit()

        print("role enum populated")
        return

    @staticmethod
    def admin_user():

        user_key : int = 100000

        #generate salt and hash
        salt : bytes                    = bcrypt.gensalt(rounds = SALT_ROUNDS)
        hashed_password : bytes         = bcrypt.hashpw(Controller.default_admin_password.encode(ENCODING), salt)

        #endcoding for explicity
        s_salt : str                    = salt.decode(ENCODING)
        s_hashed_password : str         = hashed_password.decode(ENCODING)

        #declare user
        admin_user = users.Users(
            username        = Controller.default_admin_username,
            e_mail          = "",
            salt            = s_salt,
            password_hash   = s_hashed_password,
            comment         = "created by setup script",
            key             = user_key,
            timestamp       = int(time.time()),
        )

        base.session.add(admin_user)
        base.session.commit()

        #declare admin user
        query               = select(users.Users.id_us).select_from(users.Users).filter(users.Users.key == user_key)
        admin_id_us : int   = list(base.session.execute(query).fetchone())[0]

        query               = select(enums.User_role.id_ro).select_from(enums.User_role).filter(enums.User_role.key == 0) # 0 = admin
        admin_id_ro : int   = list(base.session.execute(query).fetchone())[0]

        admin_user_role = users.User_roles(
            fk_ro               = admin_id_ro,
            fk_us               = admin_id_us,
            key                 = user_key,
            comment             = "created by setup script",
            timestamp           = int(time.time())
        )

        base.session.add(admin_user_role)
        base.session.commit()

        print("admin user with default credentials created")
        return

if __name__ == "__main__":
    Controller.main()