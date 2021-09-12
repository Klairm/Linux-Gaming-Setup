from clint.textui import colored

from src.arch.factory import Factory as ArchFactory
from src.debian.factory import Factory as DebianFactory
from src.ubuntu.factory import Factory as UbuntuFactory


def dis_elec(situation):
    while True:
        try:
            print(colored.green("\n[1] Ubuntu / Linux Mint / Any Ubuntu-based distro\n[2] Arch / Manjaro / Any arch "
                                "derivatives\n[3] Debian / Antix / Any full Debian-based distro\n[4] Go back"))

            distro = int(input("Select an option -> "))
            factory = None

            if distro == 1:
                factory = UbuntuFactory()
            elif distro == 2:
                factory = ArchFactory()
            elif distro == 3:
                factory = DebianFactory()
            elif distro == 4:
                return
            else:
                print("Wrong option, you must choose one number")

            if factory:
                if situation == "drivers":
                    factory.driver_installer().install()
                elif situation == "programs":
                    factory.program_installer().install()

        except ValueError:
            print(colored.red("Invalid entered value"))
