import distro
import os
import sys

from clint.textui import colored


def debian_repo():
	try:
		deb_codename = distro.linux_distribution()[2].lower()  # Codename for distro, ie: buster, jessie...
		repo = "deb https://dl.winehq.org/wine-builds/debian/ {} main\n".format(deb_codename)  # Repository for wine
	
		# Check if the repo is already on the source.list file , if not add it
		if os.path.isfile('/etc/apt/sources.list.d/wineGS.list'):
			print(colored.green("Repository already found"))
		else:
			with open('/etc/apt/sources.list.d/wineGS.list', 'w+') as file:
				file.write(repo)
			file.close()
	
	except PermissionError:
		print(colored.red("For be able to add a file on /etc/apt/source.list.d/ , higher permissions is required, please run the script with sudo"))
		sys.exit(1)
	
	except:
		print(colored.red("Something went wrong, exiting program"))
		sys.exit(1)
	
	else:
		# If no error happened, execute following commands for install WINE and some dependencies
		os.system("sudo apt update")
		os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
		os.system("sudo apt install --install-recommends wine")


