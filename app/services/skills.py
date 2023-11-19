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

         #validate skill level
        skill_level_valid : bool = Validator.skill_level(int(body.key_skill_level))

        if skill_level_valid is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was given: {body.key_skill_level}"}

        #generate key
        pl_key = Generator.model_key(model = Programming_languages)
        print(pl_key)

        #write entry
        new_pl = Programming_languages(
            fk_sl       = body.key_skill_level,
            name        = body.name,
            comment     = body.comment,
            key         = pl_key,
            timestamp   = int(time.time()),
        )
        session.add(new_pl)
        session.commit()

        message : dict = {"message" : pl_key}

        return message

    @staticmethod
    def library(body, response):

        #validated skill level
        if body.key_skill_level != None:
            skill_level_valid : bool                = Validator.skill_level(body.key_skill_level)
        else:
            skill_level_valid : bool                = True

        programming_language_valid : bool       = Validator.programming_language(body.key_programming_language)

        if skill_level_valid is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was given: {body.key_skill_level}"}

        elif programming_language_valid is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid programming language key was given: {body.key_programming_language}"}

        #generate library key
        lb_key = Generator.model_key(Libraries)

        #write entry
        new_lb = Libraries(
            fk_pl       = body.key_programming_language,
            fk_sl       = body.key_skill_level,
            name        = body.name,
            comment     = body.comment,
            key         = lb_key,
            timestamp   = int(time.time())
        )

        session.add(new_lb)
        session.commit()

        message : dict = {"message" : lb_key}
        return message

class Read():

    @staticmethod
    def all_programming_languages():
        """reads all skill from the corresponing model withoug filters"""

        query = select(
            Programming_languages.key,
            Programming_languages.name,
            Programming_languages.comment,
            Skill_level.key,
            Programming_languages.timestamp,
        ).join_from(
            Programming_languages,
            Skill_level,
        )

        content = session.execute(query).fetchall()

        #foramt data
        response : list = []
        for row in content:

            item : dict = {
                "key"           : row[0],
                "name"          : row[1],
                "comment"       : row[2],
                "skill_level"   : row[3],
                "timestamp"     : row[4],
            }
            response.append(item)

        return response

    @staticmethod
    def all_libraries():
        """read all skills from the libraries table"""

        query = select(
            Libraries.key,
            Libraries.name,
            Libraries.comment,
            Skill_level.key,
            Programming_languages.key,
            Libraries.timestamp,
        ).join_from(
            Libraries,
            Programming_languages,
            Skill_level,
        )

        content = session.execute(query).fetchall()

        #foramt data
        response : list = []
        for row in content:

            item : dict = {
                "key"                   : row[0],
                "name"                  : row[1],
                "comment"               : row[2],
                "skill_level"           : row[3],
                "timestamp"             : row[4],
                "programming_language"  : row[5],
                "timestamp"             : row[6]
            }
            response.append(item)

        return response


class Update():

    @staticmethod
    def programming_language(body, response):

        #entry validation
        pl_valid_entry : bool       = Validator.programming_language(body.key)

        if pl_valid_entry is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid entry key was passed: {body.key}"}

        if body.key_skill_level != None:
            skill_level_valid : bool    = Validator.skill_level(body.key_skill_level)

            if skill_level_valid == False:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return {"message" : f"invalid skill level key was passed: {body.key_skill_level}"}

        #update entries, inefficient but it works
        value_col_matcher = [
            (body.name,                 Programming_languages.name),
            (body.key_skill_level,      Programming_languages.fk_sl),
            (body.comment,              Programming_languages.comment),
            (int(time.time()),          Programming_languages.timestamp),
        ]

        for col in value_col_matcher:

            if col[0] == None:
                continue

            session.query(Programming_languages).filter(Programming_languages.key == body.key).update({col[1] : col[0]})
            session.commit()

        #return message
        message : dict = {"message" : f"update programming language entry with key: {body.key}"}
        return message


class Delete():

    @staticmethod
    def programming_language(body, response):

        #entry validation
        pl_valid_entry : bool       = Validator.programming_language(body.key)

        if pl_valid_entry is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid entry key was passed: {body.key_skill_level}"}

        #delete entry
        session.query(Programming_languages).filter(Programming_languages.key == body.key).delete()
        session.commit()

        #return
        message : dict = {"message" : f"deleted programming_language entry with key: {body.key}"}
        return message