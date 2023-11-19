from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from db.base import Base
import time

class Programming_languages(Base):

    __tablename__ = "skills.programming_languages_pl"

    #columns
    id_pl           = Column(Integer, primary_key = True, index = True)
    fk_sl           = Column(Integer, ForeignKey("enum.skill_level_sl.id_sl", onupdate = "CASCADE"))

    name            = Column(String(75), index = True, nullable = False)
    comment         = Column(String(100), nullable = True)
    key             = Column(Integer, nullable = False, unique = True)
    timestamp       = Column(BigInteger, nullable = False)

    #relations
    skill_level     = relationship("Skill_level", foreign_keys = [fk_sl])


class Libraries(Base):

    __tablename__ = "skills.libraries_lb"

    #columns
    id_lb           = Column(Integer, primary_key = True, index = True)
    fk_pl           = Column(Integer, ForeignKey("skills.programming_languages_pl.id_pl", onupdate = "CASCADE"), nullable = False)
    fk_sl           = Column(Integer, ForeignKey("enum.skill_level_sl.id_sl", onupdate = "CASCADE"), nullable = True)

    name            = Column(String, index = True, nullable = False)
    comment         = Column(String, nullable = True)
    key             = Column(Integer, nullable = False, unique = True)
    timestamp       = Column(BigInteger, nullable = False)

    #relations
    programming_langauge        = relationship("Programming_languages", foreign_keys=[fk_pl])
    skill_level                 = relationship("Skill_level", foreign_keys = [fk_sl])
