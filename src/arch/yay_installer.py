import os
from clint.textui import colored

RED = colored.red


class YayInstaller:

    def install(self):
        if os.WEXITSTATUS(os.system("git clone https://aur.archlinux.org/yay.git")) == 127:
            git = input(print(RED(
                "Git is needed for install some programs, proceed to install Git? [Y/N] -->")))
            if git == "y" or git == "Y":
                self.factory.git_installer().install()
                os.system(
                    "git clone https://aur.archlinux.org/yay.git")
            elif git == "N" or git == "n":
                sys.exit("Installation cancelled!")
            else:
                print("Wrong option!")

        os.chdir("yay")
        os.system("makepkg -si")
        os.chdir("../")
        if os.WEXITSTATUS(os.system("rm -rf ./yay/")) in [1, 127, 126]:
            print(RED(
                "An error ocurred trying to clean yay folder, please remove manually."))
