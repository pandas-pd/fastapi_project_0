from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from db.base import Base
import time

class Users(Base):

    __tablename__ = "users.users_us"

    #columns
    id_us           = Column(Integer, primary_key = True, index = True)

    username        = Column(String(100), nullable = False)
    e_mail          = Column(String(100), nullable = True)
    salt            = Column(String(50), nullable = False)
    password_hash   = Column(String(72), nullable = False) #bcrypt limit
    comment         = Column(String(100), nullable = True)

    key             = Column(Integer, nullable = False, unique = True)
    timestamp       = Column(BigInteger, nullable = False)

    #reltaions
    #tbd


class User_roles(Base):

    __tablename__ = "users.user_roles_ur"

    id_ur           = Column(Integer, primary_key = True, index = True)
    fk_ro           = Column(Integer, ForeignKey("enum.role_ro.id_ro", onupdate = "CASCADE"), nullable = False)
    fk_us           = Column(Integer, ForeignKey("users.users_us.id_us", onupdate = "CASCADE", ondelete = "RESTRICT"))

    key             = Column(Integer, nullable = False, unique = True)
    timestamp       = Column(BigInteger, nullable = False)

    #relations
    #tbd
