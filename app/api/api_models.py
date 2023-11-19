from pydantic import BaseModel
from typing import Optional

class Skills():

    class add_programming_language(BaseModel):
        name : str
        key_skill_level : int
        comment : Optional[str]

    class update_programming_language(BaseModel):
        key : int
        name : Optional[str]
        key_skill_level : Optional[int]
        comment : Optional[str]

    class delete_programming_language(BaseModel):
        key : int
        comment : Optional[str]