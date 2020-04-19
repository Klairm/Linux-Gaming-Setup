from clint.textui import colored
import os, distro
import enableMultilib as eB
def WINE(dist):
	if dist == "arch":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Installing wine dependencies"))
		os.system("sudo pacman -S wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader --needed")
	elif dist =="ubuntu":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Enabling 32-bit architecture"))
		os.system("sudo dpkg --add-architecture i386 ")
		print(colored.green("Adding repository key for WINE"))
		os.system("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
		os.system("sudo apt-key add winehq.key")
		codename = distro.linux_distribution()[2]
		if codename.lower() == "eoan":
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
		
		elif codename.lower() == "disco":
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
		
		elif codename.lower() == "cosmic":
			
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

		elif codename.lower() == "bionic":
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

		elif codename.lower() == "xenial":
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
		os.system("sudo pacman -S lutris --needed")
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
		print(colored.green("Updating packages"))
		os.system("sudo pacman -Sy")
		print(colored.green("Enabling multilib"))
		eB.pacmanConf("program")

		print(colored.green("Installing GOverlay, optional dependencies and MangoHUD"))
		# GOverlay
		os.system("git clone https://aur.archlinux.org/goverlay-git.git")
		
		# GOverlay optinal dependencies 
		os.system("git clone https://aur.archlinux.org/vkbasalt.git")
		os.system("sudo pacman -S mesa-demos lib32-mesa-demos vulkan-tools --needed" )

		# MangoHUD
		os.system("git clone https://aur.archlinux.org/mangohud.git")
		
		if os.path.exists("./goverlay-git"):
			os.chdir("goverlay-git")
			print(colored.green("Executing PKGBUILD for goverlay-git"))
			os.system("makepkg -si")
			r = input("Did goverlay-git installed properly? [Y/N] -> ")
			if r == "Y" or r == "y":
				if os.path.exists("./vkbasalt"):
					os.chdir("vkbasalt")
					print(colored.green("Executing PKGBUILD for vkbasalt"))
					os.system("makepkg -si")
					rVk = input("Did goverlay-git installed properly? [Y/N] -> ")
					if rVk == "Y" or rVk == "y":
						print(colored.green("Everything fine"))
						pass
					elif rVk == "N" or rVk == "n":
						print("FIXME: Add error handler")
					else:
						print(colored.red("wrong option"))

			elif r == "N" or r== "n":
				print("FIXME: Add error handler")
			else:
				print(colored.red("wrong option"))
		else:	
			print(colored.red("Cannot found goverlay-git directory"))

	elif dist == "ubuntu":
		mHUDGOInst()		
	elif dist == "debian":
		mHUDGOInst()
	else:
		print("FIXME: Add more distros?")



def mHUDGOInst():
	if os.path.isfile("/usr/bin/mangohud"):
		print(colored.green("MangoHud already installed, proceeding to install GOverlay"))
		if os.path.isfile("/usr/bin/goverlay"):
			print(colored.green("GOverlay already installed"))
		else:
			os.system("mkdir GOverlay")
			if os.path.exists("./GOverlay"):
				print(colored.green("Installing GOverlay..."))
				os.chdir("./GOverlay")
				# FIXME: Add an automatic update for GOverlay
				os.system("wget https://github.com/benjamimgois/goverlay/releases/download/0.3.1/goverlay_0_3_1.tar.gz")
				os.system("tar -xf goverlay_0_3_1.tar.gz")
				os.system("sudo cp goverlay /usr/bin/")
				if os.path.isfile("/usr/bin/goverlay"):
					print(colored.green("GOverlay installed succesfuly"))
				else:
					print(colored.red("Something went wrong installing GOverlay, please try again, or report the issue"))
			else:
				print(colored.red("Cannot found GOverlay directory"))
				# FIXME: Add error handler
	else:
		print(colored.green("Installing MangoHUD..."))
		os.system("mkdir MangoHUD")
		if os.path.exists("./MangoHUD"):
			os.chdir("./MangoHUD")
			# FIXME: Add an automatic update for mangohud
			os.system("wget https://github.com/flightlessmango/MangoHud/releases/download/v0.3.1/MangoHud-v0.3.1.tar.gz")
			os.system("tar -xf MangoHud-v0.3.1.tar.gz")
			if os.path.exists("./MangoHud"):
				os.chdir("./MangoHud")
				os.system("./mangohud-setup.sh install")
				if os.path.isfile("/usr/bin/mangohud"):
					print(colored.green("MangoHUD installed succesfuly"))
					mHUDGOInst()
				else:
					print(colored.red("Something went wrong installing MangoHUD, please try again, or report the issue"))
					# FIXME: Add error handler
			else:
				print(colored.red("Cannot found MangoHud directory"))
		else:
			print(colored.red("Cannot found MangoHUD directory"))

def Steam(dist):
	if dist == "arch":
		eB.pacmanConf("program")
		os.system("sudo pacman -S steam --needed")
	elif dist == "ubuntu":
		os.system("sudo apt install steam-installer")
	else:
		print(colored.red("This shouldn't happen"))
