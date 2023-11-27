from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from db.base import Base
import time

class Projects(Base):

    __tablename__ = "project.projects_pr"

    #columns
    id_pr           = Column(Integer, primary_key = True, index = True)
    fk_ps           = Column(Integer, ForeignKey("enum.project_status_ps.id_ps", onupdate = "RESTRICT"))

    name            = Column(String(100), nullable = False)
    description     = Column(String(500), nullable = True)
    sequence_number = Column(Integer, nullable = True)
    key             = Column(Integer, nullable = False, unique = True)
    link            = Column(String(250), nullable = True)

    #relationships
    porject_status  = relationship("Project_status", backref = "parent")