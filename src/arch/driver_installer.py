from clint.textui import colored
import os
import sys

RED = colored.red


class DriverInstaller:
    def install(self):
        print(RED('''
            The script will edit the /etc/pacman.conf file, for enable multilib, you can know more about multlib here:
            https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html

            '''))

        op = input("Do you want to continue? [Y/N] --> ")

        if op in ['Y', 'y']:
            os.system("sudo python3 src/enableMultilib.py  drivers")
        elif op in ['n', 'N']:
            return
