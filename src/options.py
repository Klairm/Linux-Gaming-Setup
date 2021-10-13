from clint.textui import colored

from src.arch.factory import Factory as ArchFactory
from src.debian.factory import Factory as DebianFactory
from src.ubuntu.factory import Factory as UbuntuFactory

import distro


def dis_elec(situation, sys_distro):

    try:

        if sys_distro == 0:
            print("Couldn't detect your distro please select one below: ")
            print(colored.green("\n[1] Ubuntu / Linux Mint / Any Ubuntu-based sys_distro\n[2] Arch / Manjaro / Any arch "
                                "derivatives\n[3] Debian / Antix / Any full Debian-based sys_distro\n[4] Go back"))

            sys_distro = int(input("Select an option bitch -> "))

        factory = None

        if sys_distro == 1:
            factory = UbuntuFactory()
        elif sys_distro == 2:
            factory = ArchFactory()

        elif sys_distro == 3:
            factory = DebianFactory()
        elif sys_distro == 4:
            return
        else:
            print("Wrong option!")

        if factory:
            if situation == "drivers":
                factory.driver_installer().install()

            elif situation == "programs":
                factory.program_installer().install()

    except ValueError:
        print(colored.red("Invalid entered value"))
