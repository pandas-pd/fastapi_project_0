from fastapi import APIRouter
from services.skills import *

class Endpoint():

    router = APIRouter()

    @router.get("/get_programming_languages")
    def get_programming_languages():

        content = Read.all_programming_languages()
        return content

    @router.post("/add_programming_language")
    def write_programming_language():
        pass
