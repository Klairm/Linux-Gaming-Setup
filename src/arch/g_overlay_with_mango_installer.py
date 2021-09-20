import os
import sys

from clint.textui import colored


class GOverlayWithMangoInstaller:
    def __init__(self, factory):
        self.factory = factory

    def install(self):
        print(colored.green("Updating packages"))
        os.system("sudo pacman -Sy")
        print(colored.green("Enabling multilib"))
        os.system("sudo python3 src/enableMultilib.py  program")

        # FIXME: vkBasalt required?
        print(colored.green("Installing GOverlay,and MangoHUD"))

        # GOverlay and yay installation
        if os.WEXITSTATUS(os.system("yay goverlay")) == 127:
            goverlay = input(print(
                "Seems like you don't have yay installed (it's an AUR helper for install packages from the AUR), proceed to install yay? [Y/N] ->"))

            if goverlay == "y" or goverlay == "Y":
                if os.WEXITSTATUS(os.system("git clone https://aur.archlinux.org/yay.git")) == 127:
                    git = input(print(colored.red(
                        "Cannot found Git, Git is needed for install some programs, proceed to install Git? [Y/N]")))

                    if git == "y" or git == "Y":
                        self.factory.git_installer().install()
                        os.system(
                            "git clone https://aur.archlinux.org/yay.git")
                    elif git == "N" or git == "n":
                        sys.exit("cancelled installation")
                    else:
                        print("Wrong option!")
                os.chdir("yay")

                os.system("makepkg -si")
                os.system("yay goverlay")
            elif goverlay == "n" or goverlay == "N":
                sys.exit("Installation cancelled")
            else:
                print("Wrong option!")

        os.system(
            "sudo pacman -S mesa-demos lib32-mesa-demos vulkan-tools --needed")
        os.system("yay mangohud")
