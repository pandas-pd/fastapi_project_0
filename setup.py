"""
- Creation of the virtual environment
- Installation of the needed packages
- Creating the sqlite database
- Populating the sqlite database with the needed Enum values
"""

#python libs
import os
import subprocess

#Models and session handler
from app.settings import DATABASE_URL

#from app.db.base import session
#from app.db.models.enums import *

class Setup():

    def main():

        #variables for setup
        venv_name : str     = "test_run"

        #setup venv
        venv_path       = Setup.create_venv(venv_name)
        Setup.activate_venv(venv_path)

        #setup database
        #create database
        #populate enums

    def create_venv(venv_name : str):
        """creates the venv if not already existing"""

        #generating paths for venv
        dir : str       = os.path.dirname(os.path.abspath(__file__))
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
        result : str = subprocess.run(
            command     = ["python", "-m", "venv" ,venv_path],
            text = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE
        )
        print(result)

        return venv_path

    def activate_venv(venv_path):
        """acitvate the virtual venv"""
        pass


def chat_gpt_sample():

    import subprocess

    # Specify the name of your virtual environment and the Python executable (change these as needed)
    venv_name = "my_venv"
    python_executable = "python3"  # Change to "python" or "python3" depending on your Python installation

    # Create a virtual environment
    create_venv_command = [python_executable, "-m", "venv", venv_name]
    subprocess.run(create_venv_command)

    # Activate the virtual environment (for Windows)
    activate_script = f".\\{venv_name}\\Scripts\\activate"

    # Alternatively, for Unix-like systems (e.g., Linux, macOS), you can use the following:
    # activate_script = f"source {venv_name}/bin/activate"

    subprocess.run([activate_script], shell=True)

    # Install Python modules in the virtual environment
    install_modules_command = [venv_name + "\\Scripts\\pip", "install", "module_name"]
    subprocess.run(install_modules_command)


if __name__ == "__main__":
    Setup.main()