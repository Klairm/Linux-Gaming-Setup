import os
from clint.textui import colored

RED = colored.red


class HeroicGamesInstaller:
    def install(self):
        if os.WEXITSTATUS(os.system("yay -S heroic-games-launcher-bin")) == 127:
            if input(print(RED("yay needed to install AUR packages, proceed to install it? [Y/N] -.>"))) in ["y", "Y"]:
                self.factory.yay_installer().install()
            else:
                sys.exit("Aborting installation")
            os.system("yay -S heroic-games-launcher-bin")
