import os

from clint.textui import colored


class LutrisInstaller:
    def install(self):
        print(colored.green("Adding lutris repository"))
        os.system("sudo add-apt-repository ppa:lutris-team/lutris")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install lutris")
