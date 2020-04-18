#!/usr/bin/env python3

from 	pyfiglet import Figlet
from clint.textui import colored
import options as opt
import os, platform
f = Figlet(font='speed')
print(colored.yellow(f.renderText('''
	GAME SETUP''')))


while True:
	if platform.system() != 'Linux':
		print("This is for Linux only")
		break
	print(colored.green("[1] Drivers and DXVK installation\n[2] Useful tools and programs\n[3] Exit"))
	op = int(input("Select an option -> "))
	
	if op == 1:
		opt.disElec("drivers")
	elif op == 2:
		opt.disElec("programs")
	elif op ==3:
		break
	else:
		print("Wrong option!")
