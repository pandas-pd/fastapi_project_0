from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base

class Programming_languages(Base):

    __tablename__ = "skills.programming_languages_pl"

    id_pl = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)

class Libraries(Base):

    __tablename__ = "skills.libraries_lb"

    id_lb = Column(Integer, primary_key=True, index=True)
    fk_pl = Column(Integer, ForeignKey("skills.programming_languages_pl.id_pl"), ondelete = "SET NULL")

    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)