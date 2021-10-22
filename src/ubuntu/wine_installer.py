import os
import distro

from clint.textui import colored


class WineInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        print('''WINE allows you to run Windows software in other OS, like Linux.''')
        print(GREEN("Enabling 32-bit architecture"))
        self.apt.add_architecture("i386")

        print(GREEN("Adding repository key for WINE"))
        os.system("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
        self.apt.add_key("winehq.key")

        print(GREEN("Adding repository"))
        codename = distro.linux_distribution()[2].lower()
        self.apt.add_repository(
            "'deb https://dl.winehq.org/wine-builds/ubuntu/ {} main'".format(codename))

        print(GREEN("Updating packages, installing wine and wine dependencies"))

        if os.WEXITSTATUS(os.system("sudo apt-get install --install-recommends wine-stable")) > 0:
            print(GREEN("Executing alternative command for solve a detected error"))
            self.apt.install(["winehq-stable", "wine-stable",
                             "wine-stable-i386", "wine-stable-amd64"], recommends=True)

        self.apt.install([
            "libgnutls30:i386", "libldap-2.4-2:i386", "libgpg-error0:i386", "libxml2:i386", "libasound2-plugins:i386",
            "libsdl2-2.0-0:i386", "libfreetype6:i386", "libdbus-1-3:i386", "libsqlite3-0:i386"
        ])
