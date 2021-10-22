import os
import sys

from clint.textui import colored

RED = colored.red


class FeralGameModeInstaller:
    def __init__(self, factory):
        self.factory = factory

    def clone_feral_game_mode(self):
        if os.path.exists("./Gamemode"):
            os.chdir("./Gamemode")
        else:
            os.system("mkdir Gamemode")
            os.chdir("./Gamemode")

        if os.WEXITSTATUS(os.system("git clone https://github.com/FeralInteractive/gamemode.git")) == 127:
            git = input(print(RED(
                "Cannot find Git, Git is needed for install some programs, proceed to install Git? [Y/N]")))
            if git == "y" or git == "Y":
                self.factory.git_installer().install()
                os.system(
                    "git clone https://github.com/FeralInteractive/gamemode.git")
            elif git == "n" or git == "N":
                sys.exit("Installation cancelled")

        os.chdir("gamemode")
        os.system("git checkout 1.6.1")
        os.system("sudo chmod +x bootstrap.sh")
        os.system("./bootstrap.sh")
