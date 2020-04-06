from clint.textui import colored
import brands as br
import enableMultilib as eM
import programs as pr
import os
def disElec(situation):
	while True:
		try:
			print(colored.green('''
				[1] Ubuntu / Linux Mint / Any Ubuntu-based distro
				[2] Arch / Manjaro / Any arch derivatives
				[3] Go back'''))
			distro = int(input("Select an option -> "))
			if distro == 1:
				if situation == "drivers":
					br.brandSelUbuntu()
				elif situation == "programs":
					print(colored.green('''
						[1] WINE (Essential)
						[2] Lutris
						[3] GOverlay with MangoHUD
						[4] Back
						'''))
					prgm = int(input("Select an option -> "))
					if prgm == 1:
						pr.WINE("ubuntu")
			elif distro == 2:
				if situation == "drivers":

					print(colored.red('''
						The script will edit the /etc/pacman.conf file, for enable multilib, you can know more about multlib here:
						https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html

						'''))
					op = input("Do you want to continue? [Y/N] -> ")
					if op == 'Y' or op == 'y':
						eM.pacmanConf("drivers")
				elif situation == "programs":
					print(colored.green('''
						[1] WINE (Essential)
						[2] Lutris
						[3] GOverlay with MangoHUD
						[4] Back
						'''))
					prgm = int(input("Select an option -> "))
					if prgm == 1:
						eM.pacmanConf("program")
						pr.WINE("arch")


			elif distro == 3:
				break
			else:
				print("Wrong option, you must choose one number")
		except PermissionError:
			print("Run the script as root, using: sudo GamingSetup.py")


			