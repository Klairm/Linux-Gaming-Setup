import os
import sys

from clint.textui import colored
from src.helpers import download_tarball

CONFIRM = ["y", "Y"]
DENY = ["n", "N"]


class GOverlayWithMangoInstaller:
    def install(self):
        # Check if curl and jq is installed
        if os.WEXITSTATUS(os.system("jq")) == 127:
            print("jq is not installed, make sure to run the setup.sh script")
            op = input(print("Proceed to install jq,curl and wget? [Y/N] -> "))

            if op in CONFIRM:
                os.system("sudo apt install jq curl wget")
            elif op in DENY:
                sys.exit("Installation cancelled")

        self.install_mango()
        self.install_g_overlay()

    def install_mango(self):
        mango_tarball = download_tarball("flightlessmango", "MangoHud", 2)

        if os.path.isfile(mango_tarball.split()[0]):
            if os.WEXITSTATUS(os.system("tar -xf {}".format(mango_tarball))) == 2:
                sys.exit("Fatal error trying to extract the tarball")
            else:
                os.chdir("MangoHud")

                if os.WEXITSTATUS(os.system("./mangohud-setup.sh install")) == 126:
                    os.system("chmod +x mangohud-setup.sh")
                    os.system("./mangohud-setup.sh install")

                if os.path.isfile("/usr/bin/mangohud"):
                    print(colored.green("MangoHUD installed succesfully"))

        else:
            print("Cannot download MangoHud or can't locate it")

    def install_g_overlay(self):
        if os.path.isfile("/usr/bin/goverlay"):
            print(colored.green("GOverlay already installed, updating GOverlay..."))
            os.remove("/usr/bin/goverlay")

            if os.path.exists("./GOverlay"):
                os.system("rm -rf ./GOverlay")
                os.mkdir("GOverlay")
        else:
            print(colored.green("Installing GOverlay..."))
            os.system("mkdir GOverlay")

        os.chdir("./GOverlay")

        goverlay_tarball = download_tarball("benjamimgois", "goverlay", 0)

        if os.path.isfile(goverlay_tarball.split()[0]):
            if os.WEXITSTATUS(os.system("tar -xf {}".format(goverlay_tarball))) == 2:
                sys.exit("Fatal error trying to extract the tarball")
            else:
                os.system("chmod +x goverlay")

                if os.WEXITSTATUS(os.system("mv goverlay /usr/bin/")) > 0:
                    print("Error trying to move goverlay file to /us/bin/ executing command as root...")
                    os.system("sudo mv goverlay /usr/bin/")

                if os.path.isfile("/usr/bin/goverlay"):
                    print(colored.green("GOverlay installed succesfully"))
                else:
                    print("goverlay cannot be moved on /usr/bin/, you still can execute it from the current directory")
        else:
            print("GOverlay download MangoHud or can't locate it")
