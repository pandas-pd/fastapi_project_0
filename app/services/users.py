from db.base import session
from sqlalchemy import select, insert, delete, update
from fastapi import status
import time

from db.models.users import Users, User_roles
from db.models.enums import User_role

from services.helper import *

class Write():
    pass


class Read():
    pass


class Update():
    pass


class Delete():
    pass