import os


class SteamInstaller:
    def install(self):
        os.system("sudo python3 src/enableMultilib.py  program")
        os.system("sudo pacman -S steam --needed")
