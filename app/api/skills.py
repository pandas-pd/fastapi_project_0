from fastapi import APIRouter, Response, status
from services.skills import *
from api.models import Skills

class Endpoint():

    router = APIRouter()

    @router.get("/get_programming_languages", tags = ["skills"])
    def get_programming_languages():

        response = Read.all_programming_languages()
        return response

    @router.post("/add_programming_language", tags = ["skills"])
    def write_programming_language(body : Skills.add_programming_language, response: Response):

        response  = Write.programming_language(body, response)
        return response
