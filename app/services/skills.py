from db.base import session
from db.models.skills import Programming_languages, Libraries

class Write():
    pass

class Read():

    def all_programming_languages():
        """reads all skill from the corresponing model withoug filters"""

        column_names = Programming_languages.__table__.columns.keys()
        print(type(column_names))

        return {"content" : f"{column_names}"}
        #session

class Update():
    pass

class Delete():
    pass
