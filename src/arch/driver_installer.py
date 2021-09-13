from clint.textui import colored
import os


class DriverInstaller:
    def install(self):
        print(colored.red('''
            The script will edit the /etc/pacman.conf file, for enable multilib, you can know more about multlib here:
            https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html

            '''))

        op = input("Do you want to continue? [Y/N] -> ")

        if op == 'Y' or op == 'y':
            os.system("sudo python3 enableMultilib.py drivers")
