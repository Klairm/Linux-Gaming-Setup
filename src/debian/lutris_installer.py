import os

from clint.textui import colored


class LutrisInstaller:
    def install(self):
        os.system('echo "deb http://download.opensuse.org/repositories/home:/strycore/Debian_10/ ./" | sudo tee /etc/apt/sources.list.d/lutris.list')

        if os.WEXITSTATUS(os.system("wget -q https://download.opensuse.org/repositories/home:/strycore/Debian_10/Release.key -O- | sudo apt-key add -")) == 127:
            print(colored.red("Wget is not installed, proceeding to install it..."))
            os.system("sudo apt-get install wget")

        os.system("sudo apt-get update")
        os.system("sudo apt-get install lutris")
