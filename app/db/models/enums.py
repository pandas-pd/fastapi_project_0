from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Skill_level(Base):

    __tablename__ = "enum.skill_level_sl"

    #columns
    id_sl       = Column(Integer, primary_key = True, index = True)

    key         = Column(Integer, nullable = False)
    value       = Column(String(50), nullable = True)

    #relations
    children        = relationship("Programming_languages", backref = "parent")
    children        = relationship("Libraries", backref = "parent")


class Project_status(Base):

    __tablename__ = "enum.project_status_ps"

    #columns
    id_ps       = Column(Integer, primary_key = True, index = True)

    key         = Column(Integer, nullable = False)
    value       = Column(String(50), nullable = True)

    #relations
    children    = relationship("Projects", backref = "parent")


class User_role(Base):

    __tablename__ = "enum.role_ro"

    #columns
    id_ro       = Column(Integer, primary_key = True, index = True)

    key         = Column(Integer, nullable = False)
    value       = Column(String(50), nullable = False)

    #relations
    #children    = relationship("", backref = "parent")