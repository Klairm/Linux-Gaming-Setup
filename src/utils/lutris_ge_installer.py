from src.utils.helpers import download_tarball
import os
from clint.textui import colored

ERROR = [1, 2, 127, 126]

RED = colored.red
GREEN = colored.green


class LutrisGeInstaller:
    def install(self):
        os.system("mkdir -p  ~/.local/share/lutris/runners/wine/")
        lutris_ge = download_tarball("GloriousEggroll", "wine-ge-custom")
        lutris_ge = lutris_ge.split()[0].strip('""')
        if os.path.isfile(lutris_ge):
            if os.WEXITSTATUS(os.system("tar -xf {} -C ~/.local/share/lutris/runners/wine/".format(lutris_ge))) in ERROR:
                sys.exit("Error: fatal error trying to extract the tarball")
            else:
                print("Cleaning tarball...")
                if os.WEXITSTATUS(os.system("rm {}".format(lutris_ge))) in ERROR:
                    print(RED("Error: error trying to remove tarball."))
                else:
                    print(GREEN("Succesfully cleaned tarball."))
        else:
            print(RED("Something went wrong trying to localize the tarball."))
