import bcrypt

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
    def password_match(username : str, password : str) -> bool:

        #password_match : bool = bcrypt.checkpw(password_input.encode(encoding), stored_hashed_password.encode(encoding))
        pass

    @staticmethod
    def reset_password():
        pass

    def change_password():
        pass
