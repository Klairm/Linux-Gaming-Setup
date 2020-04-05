from clint.textui import colored
import brands as br
def disElec():
	while True:
		print(colored.green('''
			[1] Ubuntu / Linux Mint / Any Ubuntu-based distro
			[2] Arch / Manjaro / Any arch derivatives
			[3] Go back'''))
		distro = int(input("Select an option -> "))
		if distro == 1:
			br.brandSel()
		elif distro == 2:
			print("FIXME: Add Arch installer")
		elif distro == 3:
			break
		else:
			print("Wrong option, you must choose one number")


			