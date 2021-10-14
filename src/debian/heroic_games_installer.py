import subprocess
from clint.textui import colored


class HeroicGamesInstaller:
    def install(self):
        try:
            print(colored.yellow(
                "Executing Heroic Games Installer external script, this will take a while..."))
            p = subprocess.call(
                ['/bin/bash', '-c', 'bash <(wget -O- https://raw.githubusercontent.com/Heroic-Games-Launcher/HeroicGamesLauncher/main/madrepo.sh)'])
            if p == 0:
                print(colored.green("Installed Heroic Games Launcher succesfully."))
        except subprocess.CalledProcessError:
            print(colored.red("ERROR: Something went wrong."))
