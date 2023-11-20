from fastapi import APIRouter, Response, status
from services.skills import *
from api.api_models import Skills

class Endpoint():

    router = APIRouter()

    # Programming Languages

    @router.post("/add_programming_language", tags = ["skills"])
    def add_programming_language(body : Skills.add_programming_language, response : Response):

        response  = Write.programming_language(body, response)
        return response

    @router.get("/get_programming_languages", tags = ["skills"])
    def get_programming_languages():

        response = Read.programming_languages()
        return response

    @router.put("/update_programming_language", tags = ["skills"])
    def update_programming_language(body : Skills.update_programming_language, response : Response):

        response = Update.programming_language(body, response)
        return response

    @router.delete("/delete_programming_language", tags = ["skills"])
    def delete_programming_language(body : Skills.delete_programming_language, response : Response):

        response = Delete.programming_language(body, response)
        return response

    # Libraries

    @router.post("/add_library", tags = ["skills"])
    def add_library(body : Skills.add_library, response : Response):

        response = Write.library(body, response)
        return response

    @router.get("/get_libraries/", tags = ["skills"])
    def get_libraries(key_programming_language : int = None):

        response = Read.libraries(key_programming_language)
        return response

    @router.put("/update_library", tags = ["skills"])
    def update_library(body : Skills.update_library, response : Response):

        response = Update.library(body, response)
        return response