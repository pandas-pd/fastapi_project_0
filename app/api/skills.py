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

        response = Read.all_programming_languages()
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

