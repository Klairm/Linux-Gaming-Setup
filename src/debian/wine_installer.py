import os

from clint.textui import colored
from src import addRepo


class WineInstaller:
    def install(self):
        print('''WINE allows you to run Windows software in other OS, like Linux.''')
        print(colored.green("Enabling 32-bit architecture"))

        os.system("sudo dpkg --add-architecture i386")

        if os.WEXITSTATUS(os.system("wget -nc https://dl.winehq.org/wine-builds/Release.key")) == 127:
            print(colored.red("Wget is not installed, proceeding to install it..."))
            os.system("sudo apt-get install wget")

        os.system("sudo apt-key add Release.key")

        addRepo.debian_repo()
