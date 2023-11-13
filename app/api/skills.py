from fastapi import APIRouter
from services.skills import *

class Endpoint():

    router = APIRouter()

    @router.get("/get_programming_languages", tags = ["skills"])
    def get_programming_languages():

        content = Read.all_programming_languages()
        return content

    @router.post("/add_programming_language", tags = ["skills"])
    def write_programming_language():
        pass
