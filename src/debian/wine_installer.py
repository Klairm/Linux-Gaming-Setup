import os
import sys

import distro
from clint.textui import colored
RED = colored.red
GREEN = colored.green


class WineInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        print('''WINE allows you to run Windows software in other OS, like Linux.''')

        if os.WEXITSTATUS(os.system("wget -nc https://dl.winehq.org/wine-builds/Release.key")) == 127:
            print(RED("Wget is not installed, proceeding to install it..."))
            self.apt.install(["wget"])
            os.system("wget -nc https://dl.winehq.org/wine-builds/Release.key")

        self.apt.add_key("Release.key")

        print(GREEN("Enabling 32-bit architecture"))
        self.apt.add_architecture("i386")

        try:
            # Codename for distro, ie: buster, jessie...
            deb_codename = distro.linux_distribution()[2].lower()
            # Repository for wine
            repo = "deb https://dl.winehq.org/wine-builds/debian/ {} main\n".format(
                deb_codename)

            # Check if the repo is already on the source.list file , if not add it
            if os.path.isfile('/etc/apt/sources.list.d/wineGS.list'):
                print(GREEN("Repository already found"))
            else:
                with open('/etc/apt/sources.list.d/wineGS.list', 'w+') as file:
                    file.write(repo)
                file.close()

        except PermissionError:
            print(RED(
                "For be able to add a file on /etc/apt/source.list.d/ , higher permissions is required, please run the script with sudo"))
            sys.exit(1)

        except:
            print(RED("Something went wrong, exiting program"))
            sys.exit(1)

        else:
            self.apt.install(["libgnutls30:i386", "libldap-2.4-2:i386", "libgpg-error0:i386", "libxml2:i386",
                              "libasound2-plugins:i386", "libsdl2-2.0-0:i386", "libfreetype6:i386", "libdbus-1-3:i386",
                              "libsqlite3-0:i386"])

            self.apt.install(["wine"], recommends=True)
