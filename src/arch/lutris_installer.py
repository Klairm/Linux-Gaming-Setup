import os

from clint.textui import colored


class LutrisInstaller:
    def install(self):
        print(colored.green("Installing lutris"))
        os.system("sudo pacman -S lutris --needed")
