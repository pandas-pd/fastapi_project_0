from fastapi import APIRouter, Response, status
from services.skills import *
from api.api_models import Skills

class Endpoint():

    router = APIRouter()

    # Programming Languages

    @router.post("/skills/programming_language", tags = ["programming_language"])
    def add_programming_language(body : Skills.add_programming_language, response : Response):

        response  = Write.programming_language(body, response)
        return response

    @router.get("/skills/programming_language", tags = ["programming_language"])
    def get_programming_languages():

        response = Read.programming_languages()
        return response

    @router.put("/skills/programming_language", tags = ["programming_language"])
    def update_programming_language(body : Skills.update_programming_language, response : Response):

        response = Update.programming_language(body, response)
        return response

    @router.delete("/skills/programming_language", tags = ["programming_language"])
    def delete_programming_language(body : Skills.delete_programming_language, response : Response):

        response = Delete.programming_language(body, response)
        return response

    # Libraries

    @router.post("/skills/library", tags = ["library"])
    def add_library(body : Skills.add_library, response : Response):

        response = Write.library(body, response)
        return response

    @router.get("/skills/library/", tags = ["library"])
    def get_libraries(key_programming_language : int, response : Response):

        response = Read.libraries(key_programming_language, response)
        return response

    @router.put("/skills/library", tags = ["library"])
    def update_library(body : Skills.update_library, response : Response):

        response = Update.library(body, response)
        return response

    @router.delete("/skills/library", tags = ["library"])
    def delete_library(body: Skills.delete_library, response : Response):

        response = Delete.library(body, response)
        return response