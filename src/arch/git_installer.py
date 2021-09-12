import os


class GitInstaller:
    def install(self):
        os.system("sudo pacman -S git")
