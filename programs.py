from clint.textui import colored
import os, distro
def WINE(dist):
	if dist == "arch":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Installing wine dependencies"))
		os.system("sudo pacman -S wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader")
	elif dist =="ubuntu":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Enabling 32-bit architecture"))
		os.system("sudo dpkg --add-architecture i386 ")
		print(colored.green("Adding repository key for WINE"))
		os.system("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
		os.system("sudo apt-key add winehq.key")
		nameDistro = distro.linux_distribution[0]
		verDistro = distro.linux_distribution[1]
		if float(verDistro) == 19.10 and nameDistro == "Ubuntu":
			print(colored.green("Adding repository"))
			os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'")
			print(colored.green("Updating packages, installing wine and wine dependencies"))
			os.system("sudo apt-get update")
			os.system("sudo apt-get install --install-recommends wine-stable")
			op = input("Did you received this error? -> The following packages have unmet dependencies [Y/N] -> ")
			if op == "Y" or op == "y":
				print(colored.green("Executing alternative command for solve that error"))
				os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
			elif op == "N" or op == "n":
				print(colored.green("Proceeding to continue"))
			else:
				print(colored.red("Wrong option"))
					
			os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
		
		elif float(verDistro) == 19.04 and nameDistro == "Ubuntu":
			print(colored.green("Adding repository"))
			os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ disco main'")
			print(colored.green("Updating packages, installing wine and wine dependencies"))
			os.system("sudo apt-get update")
			os.system("sudo apt-get install --install-recommends winehq-stable")
			p = input("Did you received this error? -> The following packages have unmet dependencies [Y/N] -> ")
			if op == "Y" or op == "y":
				print(colored.green("Executing alternative command for solve that error"))
				os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
			elif op == "N" or op == "n":
				print(colored.green("Continuing"))
			else:
				print(colored.red("Wrong option"))
				
			os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
		
		elif float(verDistro) == 18.10 and nameDistro == "Ubuntu":
			
			print(colored.green("Adding repository"))
			os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ cosmic main'")
			print(colored.green("Updating packages, installing wine and wine dependencies"))
			os.system("sudo apt-get update")
			os.system("sudo apt-get install --install-recommends winehq-stable")
			p = input("Did you received this error? -> The following packages have unmet dependencies [Y/N] -> ")
			if op == "Y" or op == "y":
				print(colored.green("Executing alternative command for solve that error"))
				os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
			elif op == "N" or op == "n":
				print(colored.green("Continuing"))
			else:
				print(colored.red("Wrong option"))
				
			os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")

		elif (float(verDistro) == 18.04 and nameDistro == "Ubuntu") or (float(verDistro) >= 19.0 and nameDistro == "Linuxt Mint"):
			print(colored.green("Adding repository"))
			os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'")
			print(colored.green("Updating packages, installing wine and wine dependencies"))
			os.system("sudo apt-get update")
			os.system("sudo apt-get install --install-recommends winehq-stable")
			p = input("Did you received this error? -> The following packages have unmet dependencies [Y/N] -> ")
			if op == "Y" or op == "y":
				print(colored.green("Executing alternative command for solve that error"))
				os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
			elif op == "N" or op == "n":
				print(colored.green("Continuing"))
			else:
				print(colored.red("Wrong option"))
				
			os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")

		elif (float(verDistro) == 16.04 and nameDistro == "Ubuntu") or (float(verDistro) >= 18.0 and float(verDistro) < 19 and nameDistro == "Linux Mint"):
			print(colored.green("Adding repository"))
			os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main'")
			print(colored.green("Updating packages, installing wine and wine dependencies"))
			os.system("sudo apt-get update")
			os.system("sudo apt-get install --install-recommends winehq-stable")
			p = input("Did you received this error? -> The following packages have unmet dependencies [Y/N] -> ")
			if op == "Y" or op == "y":
				print(colored.green("Executing alternative command for solve that error"))
				os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
			elif op == "N" or op == "n":
				print(colored.green("Continuing"))
			else:
				print(colored.red("Wrong option"))
				
			os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
		else:
			print("FIXME: Add some handler here, or allow to manually enter the version")
	elif dist == "debian":
		print("FIXME: Add Debian/ Fulldebian-based installer")
	else:
		print("FIXME: Add more distros?")

def Lutris(dist):
	if dist == "arch":
		print(colored.green("Installing lutris"))
		os.system("sudo pacman -S lutris")
	elif dist == "ubuntu":
		print(colored.green("Adding lutris repository"))
		os.system("sudo add-apt-repository ppa:lutris-team/lutris")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install lutris")
	elif dist == "debian":
		os.system('echo "deb http://download.opensuse.org/repositories/home:/strycore/Debian_10/ ./" | sudo tee /etc/apt/sources.list.d/lutris.list')
		os.system("wget -q https://download.opensuse.org/repositories/home:/strycore/Debian_10/Release.key -O- | sudo apt-key add -")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install lutris")
	else:
		print("FIXME: Add more distros?")


def GOverlwMango(dist):
	if dist == "arch":
		print("FIXME: Add arch installer")
	elif dist == "ubuntu":
		print("FIXME: Add ubuntu installer")
	elif dist == "debian":
		print("FIXME: Add debian instaler")
	else:
		print("FIXME: Add more distros?")






