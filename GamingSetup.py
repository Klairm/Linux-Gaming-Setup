#!/usr/bin/env python3

import platform

from pyfiglet import Figlet
from clint.textui import colored
from src import options as opt


figlet = Figlet(font='speed')

print(colored.yellow(figlet.renderText('''GAME SETUP''')))

while True:
	try:
		if platform.system() != 'Linux':
			print("This is for Linux only")
			break

		print(colored.green("[1] Drivers and DXVK installation\n[2] Useful tools and programs\n[3] Exit"))
		op = int(input("Select an option -> "))
	
		if op == 1:
			opt.dis_elec("drivers")
		elif op == 2:
			opt.dis_elec("programs")
		elif op == 3:
			break
		else:
			print("Wrong option!")

	except ValueError:
		print(colored.red("Invalid entered value"))
