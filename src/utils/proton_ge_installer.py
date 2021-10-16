import os
import sys

from clint.textui import colored
from src.utils.helpers import download_tarball

CONFIRM = ["y", "Y"]
DENY = ["n", "N"]

RED = colored.red
GREEN = colored.green


class ProtonGeInstaller:
    def __init__(self, factory):
        self.factory = factory

    def install(self):
        home = os.popen("echo ~/").read()
        compat_folder = None

        # FIXME: Optimize this another if hell
        if not os.path.exists("{}.steam/root/".format(home.strip("\n"))) and not os.path.exists(
                "{}.var/app/com.valvesoftware.Steam/".format(home.strip("\n"))):
            op = input(print(
                "Steam needs to be installed for this, do you want to install Steam? [Y/N] -> "))

            if op in CONFIRM:
                self.factory.steam_installer().install()
                print(
                    "It is needed to open Steam one time for create the folders, opening steam...")
                os.system("steam")
            elif op in DENY:
                print(RED("Installation cancelled"))
            else:
                print("Wrong option!")
        elif os.path.exists("{}.steam/root/".format(home.strip("\n"))):
            print(GREEN("Detected steam installation folder on ~/.steam/"))
            steam_folder = "{}.steam/root/compatibilitytools.d/".format(
                home.strip("\n"))

            if os.path.exists(steam_folder):
                print(GREEN(
                    "compatibilitytools.d folder detected under ~/.steam/root/"))
            else:
                if os.WEXITSTATUS(os.system("mkdir ~/.steam/root/compatibilitytools.d/")) == 126:
                    print(RED(
                        "Cannot create the folder ~/.steam/root/compatibilitytools.d/, trying with sudo permissions..."))
                    os.system("sudo mkdir ~/.steam/root/compatibilitytools.d/")

            compat_folder = steam_folder
        elif os.path.exists("{}.var/app/com.valvesoftware.Steam/".format(home.strip("\n"))):
            print(GREEN(
                "Detected flatpak steam installation folder on ~/.var/app/com.valvesoftware.Steam/"))
            flatpak_steam_folder = "{}.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/".format(
                home.strip("\n"))

            if os.path.exists(flatpak_steam_folder):
                print(GREEN(
                    "compatibilitytools.d folder detected under ~/.var/app/com.valvesoftware.Steam/data/Steam/"))
            else:
                if os.WEXITSTATUS(os.system("mkdir ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/")) == 126:
                    print(RED(
                        "Cannot create the folder ~/.steam/root/compatibilitytools.d/, trying with sudo permissions..."))
                    os.system(
                        "sudo mkdir ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/")

            compat_folder = flatpak_steam_folder

        if compat_folder is None:
            sys.exit(RED("Unable to find Steam folder."))

        os.chdir(compat_folder)
        proton_ge_tarball = download_tarball(
            "GloriousEggroll", "proton-ge-custom")
        proton_ge_tarball = proton_ge_tarball.split()[0].strip('""')
        if os.WEXITSTATUS(os.system("tar -xf {}".format(proton_ge_tarball))) != 0:
            sys.exit(RED("Cannot extract the tarball"))
        else:
            print(GREEN(
                "Tarball extracted succesfully, ProtonGE is now installed, for enable it on Steam, see: https://github.com/GloriousEggroll/proton-ge-custom/#enabling"))
            print(GREEN("Cleaning the tar file..."))

            if os.WEXITSTATUS(os.system("rm {}".format(proton_ge_tarball))) != 0:
                print(RED(
                    "Cannot clean the tar file, checking the correct directory"))

                if os.getcwd() + "/" != compat_folder:
                    os.chdir(compat_folder)

                print(RED(
                    "Cannot clean the tar file, trying with sudo permissions..."))

                if os.WEXITSTATUS(os.system("sudo rm {}".format(proton_ge_tarball))) != 0:
                    print(
                        colored.red("Cannot clean the tar file, you can delete it manually on {}".format(compat_folder)))
