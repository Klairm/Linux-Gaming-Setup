from clint.textui import colored
import os
import brands as br
def pacmanConf():
	try:
		with open('/etc/pacman.conf', 'r') as file:
		    data = file.readlines()
		for i, j in enumerate(data):
			
			if j == "#[multilib]\n":
				data[i] = "[multilib]\n"
				data[i+1] = "SigLevel = PackageRequired\n"
				data[i+2] = "Include = /etc/pacman.d/mirrorlist\n"
				os.system("sudo pacman -Syu")
				br.brandSelArch()
			elif j == "[multilib]\n":
				print(colored.green('''
					Seems like multilib it's already uncommented, to be sure you can check it on /etc/pacman.conf
					You can check this site for know more about enabling multilib:
					 https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html'''))
				break
			else:
				print(colored.red('''
					Either multilib is already enabled, or the script can't find it on your /etc/pacman.conf file.
					You can check this site for know more about enabling multilib:
					 https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html'''))
				break

		with open('/etc/pacman.conf', 'w') as file:
		    file.writelines( data )
	except PermissionError:
		print(colored.red("Run the script as root, using: sudo GamingSetup.py"))