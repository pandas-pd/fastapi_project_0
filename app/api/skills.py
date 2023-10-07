from fastapi import APIRouter
from sqlalchemy.orm import Session
#from db.models.skills import Item
from db.base import session

class Endpoint():

    router = APIRouter()

    @router.get("/get_skills")
    def get_all_skills():

        return {"skill1": "hello from file"}


