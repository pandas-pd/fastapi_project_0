"""
- Creation of the virtual environment
- Installation of the needed packages
- Calling the scritp which creates and populates the database with enums (locates in app/db/setup.py)
"""

#python libs
import os
import subprocess

class Setup():

    @staticmethod
    def main():

        #variables for setup
        venv_name : str             = "venv"
        requirements_file : str     = os.path.join(
                                        os.path.dirname(os.path.abspath(__file__)),
                                        "requirements.txt"
        )

        #setup venv
        venv_path : str     = Setup.create_venv(venv_name)
        venv_active: bool   = Setup.activate_venv(venv_path)
        Setup.install_moduls(venv_name = venv_name, requirements_file = requirements_file)

        return

    @staticmethod
    def create_venv(venv_name : str):
        """creates the venv if not already existing"""

        #generating paths for venv
        dir : str           = os.path.dirname(os.path.abspath(__file__))
        venv_path : str     = os.path.join(dir, venv_name)

        try:
            conents : bool      = (len(os.listdir(venv_path)) > 0)
        except FileNotFoundError:
            conents : bool      = False

        #case handling

        if (os.path.exists(venv_path) and conents is True):
            print("Venv already exists")
            return

        elif (os.path.exists(venv_path) and conents is False):
            print("The given venv directory already exists but is empty. Direcorty will be removed")
            os.rmdir(venv_path)

        elif (os.path.exists(venv_path) is False):
            pass

        #create venv
        command     = ["python", "-m", "venv" ,venv_path]
        result : str = subprocess.run(command, text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        print(result)

        return venv_path

    @staticmethod
    def activate_venv(venv_path):
        """acitvate the virtual venv"""

        command = os.path.join(venv_path, "Scripts", "activate")

        try:
            subprocess.run(command, shell=True)

        except:
            print(f"Something went wrong when acitvating the given environment. Make the given venv path is valid\n{venv_path}")
            return False

    @staticmethod
    def install_moduls(venv_name, requirements_file):

        try:
            command = [venv_name + "\\Scripts\\pip", "install", "-r", requirements_file]
            subprocess.run(command)
        except:
            quit(f"Something went wrong while installing the moduls from {requirements_file}")

        return

if __name__ == "__main__":
    Setup.main()