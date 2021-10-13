#!/usr/bin/env python3

import platform
import distro

from pyfiglet import Figlet
from clint.textui import colored
from src import options as opt

distros = ["ubuntu", "debian", "linuxmint", "arch", "endeavouros"]
figlet = Figlet(font='speed')

print(colored.yellow(figlet.renderText('''GAME SETUP''')))

while True:
    try:
        if platform.system() != 'Linux':
            print("This is for Linux only")
            break

        print("Detecting your distro...")
    # FIXME: Too many if-else..
        if distro.id() in distros or distro.like() in distros:
            print(colored.green(
                f"[{distro.id()}] distro detected... based on {distro.like()}"))
            if distro.id() == "ubuntu" or distro.like() == "ubuntu":
                sys_distro = 1
            elif distro.id() == "arch" or distro.like() == "arch":
                sys_distro = 2
            elif distro.id() == "debian" or distro.like() == "debian" and distro.id() != "ubuntu":
                sys_distro = 3
        else:
            sys_distro = 0

        print(colored.green(
            "[1] Drivers and DXVK installation\n[2] Useful tools and programs\n[3] Exit"))
        op = int(input("Select an option -> "))

        if op == 1:
            opt.dis_elec("drivers", sys_distro)
        elif op == 2:
            opt.dis_elec("programs", sys_distro)
        elif op == 3:
            break
        else:
            print("Wrong option!")

    except ValueError:
        print(colored.red("Invalid entered value"))
