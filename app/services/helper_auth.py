import bcrypt
from db.base import session
from sqlalchemy import select, insert, delete, update

from db.models.users import Users
from settings import ENCODING, SALT_ROUNDS


class Password_handler():

    @staticmethod
    def salt_and_hash(password : str) -> str:

        #generate salt and hash
        salt : bytes                    = bcrypt.gensalt(rounds = SALT_ROUNDS)
        hashed_password : bytes         = bcrypt.hashpw(password.encode(ENCODING), salt)

        #endcoding for explicity
        s_salt : str                    = salt.decode(ENCODING)
        s_hashed_password : str         = hashed_password.decode(ENCODING)

        return s_salt, s_hashed_password

    @staticmethod
    def password_match(password : str, username : str = None, user_key : int = None) -> bool:

        #retrieve password hash with salt
        if (user_key != None):
            query = select(Users.password_hash).select_from(Users).filter(Users.key == user_key)

        elif (username != None):
            query = select(Users.password_hash).select_from(Users).filter(Users.username == username)

        content                 = session.execute(query).fetchone()
        hashed_password :str    = content[0]

        password_match : bool   = bcrypt.checkpw(password.encode(ENCODING), hashed_password.encode(ENCODING))
        return password_match