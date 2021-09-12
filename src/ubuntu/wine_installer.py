import os
import distro

from clint.textui import colored


class WineInstaller:
    def install(self):
        print('''WINE allows you to run Windows software in other OS, like Linux.''')
        print(colored.green("Enabling 32-bit architecture"))
        os.system("sudo dpkg --add-architecture i386 ")

        print(colored.green("Adding repository key for WINE"))
        os.system("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
        os.system("sudo apt-key add winehq.key")
        codename = distro.linux_distribution()[2].lower()

        print(colored.green("Adding repository"))
        os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ {} main'".format(codename))

        print(colored.green("Updating packages, installing wine and wine dependencies"))
        os.system("sudo apt-get update")

        if os.WEXITSTATUS(os.system("sudo apt-get install --install-recommends wine-stable")) > 0:
            print(colored.green("Executing alternative command for solve a detected error"))
            os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")

        os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
