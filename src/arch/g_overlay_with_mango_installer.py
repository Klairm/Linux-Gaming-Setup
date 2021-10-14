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

        # GOverlay installation via yay
        if os.WEXITSTATUS(os.system("yay goverlay")) == 127:
            if input(print(colored.red("yay needed to install AUR packages, proceed to install it? [Y/N] -.>"))) in ["y", "Y"]:
                self.factory.yay_installer().install()
            else:
                sys.exit("Aborting installation")

        os.system(
            "sudo pacman -S mesa-demos lib32-mesa-demos vulkan-tools --needed")
        os.system("yay goverlay")
        os.system("yay mangohud")
