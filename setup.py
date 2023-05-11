import subprocess
import urllib.request


def check_internet(host="https://google.com"):
    """
    Function to check if the system is connected to the Internet.
    """
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def setup_module(module_name):
    """
    Function to install the required python module.
    """
    # updating pip to latest version
    subprocess.run("python -m pip install --upgrade pip")

    # install required modules
    process = subprocess.run(["python3", "-m", "pip", "install", module_name])

    if process.returncode != 0:
        if not check_internet():
            print("Error!! Occurred check\nInternet Connection.")
        else:
            print("Error!! Occurred check\nModule Name.")
    else:
        print(f"{module_name} is installed successfully.")


def install_required_modules():
    print("Installing")
    print("Please wait....")
    print("Do not close this program")

    with open("requirements.txt") as file:
        for line in file:
            setup_module(line.strip())

    print("Installation finished")
    subprocess.run(["python3", "main.py"])


if __name__ == "__main__":
    install_required_modules()
