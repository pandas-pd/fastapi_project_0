from pydantic import BaseModel
from typing import Optional

class Skills():

    class add_programming_language(BaseModel):
        name : str
        skill_level : int
        comment : Optional[str]