import os

from clint.textui import colored

GREEN = colored.green

class LutrisInstaller:
    def install(self):
        print(GREEN("Installing lutris"))
        os.system("sudo pacman -S lutris --needed")
