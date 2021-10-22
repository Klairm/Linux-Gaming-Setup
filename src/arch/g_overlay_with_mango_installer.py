import os
import sys

from clint.textui import colored

RED = colored.red
GREEN = colored.green


class GOverlayWithMangoInstaller:
    def __init__(self, factory):
        self.factory = factory

    def install(self):
        print(GREEN("Updating packages"))
        os.system("sudo pacman -Sy")
        print(GREEN("Enabling multilib"))
        os.system("sudo python3 src/enableMultilib.py  program")

        # FIXME: vkBasalt required?
        print(GREEN("Installing GOverlay,and MangoHUD"))

        # GOverlay installation via yay
        if os.WEXITSTATUS(os.system("yay goverlay")) == 127:
            if input(print(RED("yay needed to install AUR packages, proceed to install it? [Y/N] -.>"))) in ["y", "Y"]:
                self.factory.yay_installer().install()
            else:
                sys.exit("Aborting installation")

        os.system(
            "sudo pacman -S mesa-demos lib32-mesa-demos vulkan-tools --needed")
        os.system("yay goverlay")
        os.system("yay mangohud")
