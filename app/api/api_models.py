from pydantic import BaseModel
from typing import Optional

class Skills():

    class add_programming_language(BaseModel):
        name : str
        key_skill_level : int
        comment : Optional[str]

    class update_programming_language(BaseModel):
        key : int
        name : str
        key_skill_level : int
        comment : Optional[str]

    class delete_programming_language(BaseModel):
        key : int

    class add_library(BaseModel):
        name : str
        key_programming_language : int
        key_skill_level : Optional[int]
        comment : Optional[str]

    class update_library(BaseModel):
        key : int
        name : str
        key_skill_level : Optional[int]
        comment : Optional[str]

    class delete_library(BaseModel):
        key : int


class Projects():

    class add_project(BaseModel):
        name : str
        description : str
        sequence_number : Optional[int]
        link : Optional[str]
        key_project_status : int

    class update_project(BaseModel):
        key : int
        name : str
        description : Optional[str]
        sequence_number : Optional[int]
        link : Optional[str]
        key_project_status : int

    class delete_project(BaseModel):
        key : int

class Users():

    class add_user(BaseModel):
        username : str
        e_mail : str
        password : str
        comment : Optional[str]

    class update_user(BaseModel):
        key : int
        username : str
        e_mail : str
        comment : Optional[str]

    class update_password(BaseModel):
        key : int
        password : str
        comment : Optional[str]

    class delete_user(BaseModel):
        key : int

class Passwords():

    class reset_password(BaseModel):
        pass

    class update_password(BaseModel):
        pass

class Roles():

    class add_role(BaseModel):
        key_role : int
        key_user : int
        comment : Optional(str)

    class delete_role(BaseModel):
        key : int
