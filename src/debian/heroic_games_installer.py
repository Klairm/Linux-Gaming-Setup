import subprocess
from clint.textui import colored

RED = colored.red
GREEN = colored.green


class HeroicGamesInstaller:
    def install(self):
        try:
            print(colored.yellow(
                "Executing Heroic Games Installer external script, this will take a while..."))
            p = subprocess.call(
                ['/bin/bash', '-c', 'bash <(wget -O- https://raw.githubusercontent.com/Heroic-Games-Launcher/HeroicGamesLauncher/main/madrepo.sh)'])
            if p == 0:
                print(GREEN("Installed Heroic Games Launcher succesfully."))
        except subprocess.CalledProcessError:
            print(RED("ERROR: Something went wrong."))
