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

        #validte key
        if (Validator.skill_level(int(body.key_skill_level)) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was given: {body.key_skill_level}"}

        #generate key and fetch keys
        pl_key = DB.generate_model_key(model = Programming_languages)
        fk_sl = Key_to_id.skill_level(key = body.key_skill_level)

        #write entry
        new_pl = Programming_languages(
            fk_sl       = fk_sl,
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
            body.key_skill_level                    = 0 # 0 = undefined

        if skill_level_valid is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was given: {body.key_skill_level}"}

        elif Validator.programming_language(body.key_programming_language) is False:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid programming language key was given: {body.key_programming_language}"}

        #generate library key and fetch programming language ids
        lb_key = DB.generate_model_key(Libraries)
        fk_pl = Key_to_id.programming_languages(body.key_programming_language)
        fk_sl = Key_to_id.skill_level(body.key_skill_level)

        #write entry
        new_lb = Libraries(
            fk_pl       = fk_pl,
            fk_sl       = fk_sl,
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
    def programming_languages():
        """reads all skill from the corresponing model withoug filters"""

        query = select(
            Programming_languages.key,
            Programming_languages.name,
            Programming_languages.comment,
            Skill_level.key,
            Programming_languages.timestamp,
        ).select_from(Programming_languages
        ).join(Skill_level, isouter = False)

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
    def libraries(key_programming_language : int, response):
        """read all skills from the libraries table"""

        #validation
        if (Validator.programming_language(key = key_programming_language) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid porgramming_language key was provided: {key_programming_language}"}

        query = select(
            Libraries.key,
            Libraries.name,
            Libraries.comment,
            Skill_level.key,
            Libraries.timestamp,
        ).select_from(Libraries
        ).join(Programming_languages, Libraries.programming_langauge, isouter = True
        ).join(Skill_level, Libraries.skill_level, isouter = True
        ).filter(Programming_languages.key == key_programming_language)

        content = session.execute(query).fetchall()

        #format data
        response : list = []

        for row in content:

            response.append({
                "key_library"               : row[0],
                "name_library"              : row[1],
                "comment"                   : row[2],
                "skill_level"               : row[3],
                "timestamp"                 : row[4],
            })

        return response


class Update():

    @staticmethod
    def programming_language(body, response):

        #validation
        if (Validator.programming_language(body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid entry key was passed: {body.key}"}

        if (Validator.skill_level(body.key_skill_level) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was passed: {body.key_skill_level}"}

        #fetch_key
        fk_sl = Key_to_id.skill_level(key = body.key_skill_level)

        #update entries, inefficient but it works
        session.query(Projects).filter(Projects.key == body.key).update({
            Programming_languages.name          : body.name,
            Programming_languages.fk_sl         : fk_sl,
            Programming_languages.comment       : body.comment,
            Programming_languages.timestamp     : int(time.time())
        })
        session.commit()

        #return message
        message : dict = {"message" : f"update programming language entry with key: {body.key}"}
        return message

    @staticmethod
    def library(body, response):

        #validation entry and skill level key
        if (Validator.library(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid entry key was passed: {body.key}"}

        elif ((body.key_skill_level != None) and (Validator.skill_level(key = body.key_skill_level) == False)):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid skill level key was passed: {body.key_skill_level}"}

        #translate key
        if (body.key_skill_level != None):
            fk_sl = Key_to_id.skill_level(key = body.key_skill_level)
        else:
            fk_sl = None

        #update entries, inefficient but it works
        session.query(Libraries).filter(Libraries.key == body.key).update({
            Libraries.name              : body.name,
            Libraries.fk_sl             : fk_sl,
            Libraries.comment           : body.comment,
            Libraries.timestamp         : int(time.time()),
        })
        session.commit()

        #return message
        message : dict = {"message" : f"update library language entry with key: {body.key}"}
        return message


class Delete():

    @staticmethod
    def programming_language(body, response):
        """deletes all library entries as well"""

        #validate entry
        if (Validator.programming_language(body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid entry key was passed: {body.key}"}

        #delete entry
        session.query(Programming_languages).filter(Programming_languages.key == body.key).delete()
        session.commit()

        #implement that all added libs will be deleted

        #return
        return {"message" : f"deleted programming_language entry with key: {body.key}"}

    @staticmethod
    def library(body, response):

        #validate entry
        if (Validator.library(key = body.key) == False):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message" : f"invalid entry key was passes: {body.key}"}

        session.query(Libraries).filter(Libraries.key == body.key).delete()
        session.commit()

        return {"message" : f"deleted libray entry with key: {body.key}"}
