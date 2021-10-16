import os
import sys

from clint.textui import colored
from src.utils.helpers import download_tarball
import distro
CONFIRM = ["y", "Y"]
DENY = ["n", "N"]
RED = colored.red
GREEN = colored.green


class GOverlayWithMangoInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        if int(distro.major_version()) >= 11 and distro.id() == "debian":
            self.apt.install(["mangohud", "goverlay"])
        elif int(distro.major_version()) >= 20 and distro.id() == "ubuntu":
            self.apt.add_repository("ppa:flexiondotorg/mangohud")
            self.apt.update()
            self.apt.install(["goverlay"])
            self.install_mango()
        else:
            # Check if curl and jq is installed
            if os.WEXITSTATUS(os.system("jq --version")) == 127:
                print("jq is not installed, make sure to run the setup.sh script")
                op = input(
                    print("Proceed to install jq, curl and wget? [Y/N] -> "))

                if op in CONFIRM:
                    self.apt.install(["jq", "curl", "wget"])
                elif op in DENY:
                    sys.exit("Installation cancelled")

            self.install_mango()
            self.install_g_overlay()

    def install_mango(self):
        mango_tarball = download_tarball(
            "flightlessmango", "MangoHud")
        mango_tarball = mango_tarball.split()[0].strip('""')
        if os.path.isfile(mango_tarball):

            if os.WEXITSTATUS(os.system("tar -xf {}".format(mango_tarball))) == 2:
                sys.exit("Fatal error trying to extract the tarball")
            else:
                os.chdir("MangoHud")

                if os.WEXITSTATUS(os.system("./mangohud-setup.sh install")) == 126:
                    os.system("chmod +x mangohud-setup.sh")
                    os.system("./mangohud-setup.sh install")

                if os.path.isfile("/usr/bin/mangohud"):
                    print(GREEN("MangoHUD installed succesfully"))

        else:
            print(RED("Something went wrong locating MangoHUD"))

    def install_g_overlay(self):
        if os.path.isfile("/usr/bin/goverlay"):
            print(GREEN("GOverlay already installed, updating GOverlay..."))
            os.remove("/usr/bin/goverlay")

            if os.path.exists("./GOverlay"):
                os.system("rm -rf ./GOverlay")
                os.mkdir("GOverlay")
        else:
            print(GREEN("Installing GOverlay..."))
            os.system("mkdir GOverlay")

        os.chdir("./GOverlay")

        goverlay_tarball = download_tarball(
            "benjamimgois", "goverlay")
        goverlay_tarball = goverlay_tarball.split()[0].strip('""')
        if os.path.isfile(goverlay_tarball):
            if os.WEXITSTATUS(os.system("tar -xf {}".format(goverlay_tarball))) == 2:
                sys.exit("Fatal error trying to extract the tarball")
            else:
                os.system("chmod +x goverlay")

                if os.WEXITSTATUS(os.system("mv goverlay /usr/bin/")) > 0:
                    print(
                        "Error trying to move goverlay file to /us/bin/ executing command as root...")
                    os.system("sudo mv goverlay /usr/bin/")

                if os.path.isfile("/usr/bin/goverlay"):
                    print(GREEN("GOverlay installed succesfully"))
                else:
                    print(
                        "goverlay cannot be moved on /usr/bin/, you still can execute it from the current directory")
        else:
            print(RED("Something went wrong locating GOverlay"))
