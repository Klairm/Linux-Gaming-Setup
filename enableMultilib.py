import os, sys
import brands as br


def pacmanConf(situation):
	
	try:
		with open('/etc/pacman.conf', 'r') as file:
		    data = file.readlines()
		    dataBac = file.readlines()
		with open('/etc/pacman.conf.backupFromGamingSetup', 'w') as file:
		    file.writelines(dataBac)

		for i, j in enumerate(data):
			
			if j == "#[multilib]\n":
				data[i] = "[multilib]\n"
				data[i+1] = "SigLevel = PackageRequired\n"
				data[i+2] = "Include = /etc/pacman.d/mirrorlist\n"
				os.system("sudo pacman -Syu")
				if situation == "drivers":
					br.brandSelArch()
				elif situation == "program":
					pass
					
			elif j == "[multilib]\n":
				print(('''
					Seems like multilib it's already uncommented, to be sure you can check it on /etc/pacman.conf
					You can check this site for know more about enabling multilib:
					 https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html'''))
				if situation == "drivers":
					br.brandSelArch()
				break

			else:
				print("Either multilib is already enabled, or the script can't find it on your /etc/pacman.conf file\n You can check this site for know more about enabling multilib:\n https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html")
				if situation == "drivers":
					br.brandSelArch()
				break

		with open('/etc/pacman.conf', 'w') as file:
			file.writelines(data)
	
	except IOError:
		print("Something went wrong trying to open the file /etc/pacman.conf")

pacmanConf(sys.argv[1])