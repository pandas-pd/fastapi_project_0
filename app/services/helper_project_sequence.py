from db.base import session
from sqlalchemy import select, insert, delete, update, and_, func
from db.models.projects import Projects

class Sequence_logic():

    @staticmethod
    def sequence_update_on_insert(tbi_sequence_number : int) -> None:
        """shifts the sequence number of the projects table when inserting an entry"""

        #update sequence numbers to keep everything in odrer
        session.query(Projects).filter(and_(
            Projects.sequence_number != None,
            Projects.sequence_number >= tbi_sequence_number,
        )).update(
            {Projects.sequence_number : Projects.sequence_number + 1}
        )
        session.commit()

        return

    @staticmethod
    def sequence_update_on_update(new_sequence_number, key : int) -> None:
        """shifts the sequence number of the projects table when updateing an entry"""

        #fetch old seucence number
        query                       = select(Projects.sequence_number).select_from(Projects).filter(Projects.key == key)
        content                     = session.execute(query).fetchone()
        old_sequence_number         = content[0] #can be int or None

        if (old_sequence_number == None) and (new_sequence_number == None):
            return

        elif (old_sequence_number == None) and (new_sequence_number != None):

            session.query(Projects).filter(Projects.sequence_number >= new_sequence_number
            ).update({Projects.sequence_number : Projects.sequence_number + 1})
            session.commit()

        elif (old_sequence_number != None) and (new_sequence_number == None):

            #shift all else -1, according to old sequence number
            session.query(Projects).filter(Projects.sequence_number > old_sequence_number
            ).update({Projects.sequence_number : Projects.sequence_number - 1})
            session.commit()

        #case both not None
        elif (old_sequence_number < new_sequence_number): # case 1

            #apply shift for all needed number to -1, expect entry to be updated
            session.query(Projects).filter(and_(
                Projects.sequence_number <= new_sequence_number,
                Projects.sequence_number > old_sequence_number,
                Projects.key != key) #extra precaution
            ).update({Projects.sequence_number : Projects.sequence_number -1})
            session.commit()

        elif (old_sequence_number > new_sequence_number): # case 2

            #apply shift for all needed number to +1, expect entry to be updated
            session.query(Projects).filter(and_(
                Projects.sequence_number >= new_sequence_number,
                Projects.sequence_number < old_sequence_number,
                Projects.key != key)
            ).update({Projects.sequence_number : Projects.sequence_number +1})
            session.commit()

        session.query(Projects).filter(Projects.key == key).update({Projects.sequence_number : new_sequence_number})
        session.commit()

        return

    @staticmethod
    def sequence_update_on_delete(key : int) -> None:
        """shifts the sequence number of the projects table when deleting an entry"""

        #fetch data
        query                           = select(Projects.sequence_number).select_from(Projects).filter(Projects.key == key)
        content                         = session.execute(query).fetchone()
        sequence_number_tbd : int       = content[0]

        #no changes needed
        if (sequence_number_tbd == None):
            return

        session.query(Projects).filter(Projects.sequence_number > sequence_number_tbd).update({
            Projects.sequence_number : Projects.sequence_number - 1,
        })
        session.commit()

        return

    @staticmethod
    def adjust_payload_sequence_number(sequence_number : int, insert : bool = True) -> int:
        """shift vlaues to max if needed"""

        #fetch data and order it
        query                           = select(func.max(Projects.sequence_number)).select_from(Projects)
        content                         = session.execute(query).fetchone()
        max_sequence_number : int       = content[0]

        #calculate new seq number for them to be in a row
        if (max_sequence_number == None):
            return 1

        elif (insert == True) and (sequence_number > max_sequence_number + 1):
            return max_sequence_number + 1

        elif (insert == False) and (sequence_number > max_sequence_number):
            return max_sequence_number

        else:
            return sequence_number