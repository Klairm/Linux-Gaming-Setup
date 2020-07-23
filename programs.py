from clint.textui import colored
import os, distro,sys
import addRepo

CONFIRM = ["y","Y"]
DENY = ["n","N"]

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
		codename = distro.linux_distribution()[2].lower()		
		print(colored.green("Adding repository"))
		os.system("sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ {} main'".format(codename))
		print(colored.green("Updating packages, installing wine and wine dependencies"))
		os.system("sudo apt-get update")
		if os.WEXITSTATUS(os.system("sudo apt-get install --install-recommends wine-stable")) > 0:
			print(colored.green("Executing alternative command for solve a detected error"))
			os.system("sudo apt-get install --install-recommends winehq-stable wine-stable wine-stable-i386 wine-stable-amd64")
		os.system("sudo apt-get install libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
		
	elif dist == "debian":
		print('''WINE allows you to run Windows software in other OS, like Linux.''')
		print(colored.green("Enabling 32-bit architecture"))
		os.system("sudo dpkg --add-architecture i386")
		if os.WEXITSTATUS(os.system("wget -nc https://dl.winehq.org/wine-builds/Release.key")) == 127:
			print(colored.red("Wget is not installed, proceeding to install it..."))
			os.system("sudo apt-get install wget")
		os.system("sudo apt-key add Release.key")
		addRepo.debianRepo()
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
		if os.WEXITSTATUS(os.system("wget -q https://download.opensuse.org/repositories/home:/strycore/Debian_10/Release.key -O- | sudo apt-key add -")) == 127:
			print(colored.red("Wget is not installed, proceeding to install it..."))
			os.system("sudo apt-get install wget")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install lutris")
	else:
		print("FIXME: Add more distros?")


def GOverlwMango(dist):
	if dist == "arch":
		print(colored.green("Updating packages"))
		os.system("sudo pacman -Sy")
		print(colored.green("Enabling multilib"))
		os.system("sudo python3 enableMultilib.py program")

		print(colored.green("Installing GOverlay,and MangoHUD"))  #FIXME: vkBasalt required?
		
		# GOverlay and yay installation
		if os.WEXITSTATUS(os.system("yay goverlay")) == 127:
			goverlay = input(print("Seems like you don't have yay installed (it's an AUR helper for install packages from the AUR), proceed to install yay? [Y/N] ->"))
			if goverlay == "y" or goverlay == "Y":
				if os.WEXITSTATUS(os.system("git clone https://aur.archlinux.org/yay.git")) == 127:
					git = input(print(colored.red("Cannot found Git, Git is needed for install some programs, proceed to install Git? [Y/N]")))
					if git == "y" or git=="Y":
						Git("arch")
						os.system("git clone https://aur.archlinux.org/yay.git")
					elif git == "N" or git == "n":
						sys.exit("cancelled installation")
					else:
						print("Wrong option!")
				os.chdir("yay")		
				os.system("makepkg -si")
				os.system("yay goverlay")
			elif goverlay == "n" or goverlay == "N":
				sys.exit("Installation cancelled")
			else:
				print("Wrong option!")
		os.system("sudo pacman -S mesa-demos lib32-mesa-demos vulkan-tools --needed" )
		os.system("yay mangohud")
	elif dist == "ubuntu":
		mHUDGOInst()		
	elif dist == "debian":
		mHUDGOInst()
	else:
		print("FIXME: Add more distros?")


def mHUDGOInst():
	# Check if curl and jq is installed
	if os.WEXITSTATUS(os.system("jq")) == 127:
		print("jq is not installed, make sure to run the setup.sh script")
		op = input(print("Proceed to install jq,curl and wget? [Y/N] -> "))
		if op in CONFIRM:
			os.system("sudo apt install jq curl wget")
		elif op in DENY:
			sys.exit("Installation cancelled")
	mangoTarball = downloadTarball("flightlessmangom","MangoHud",2)
	if os.path.isfile(mangoTarball.split()[0]):
		if os.WEXITSTATUS(os.system("tar -xf {}".format(mangoTarball))) == 2:
			sys.exit("Fatal error trying to extract the tarball")
		else:
			os.chdir("MangoHud")
			if os.WEXITSTATUS(os.system("./mangohud-setup.sh install")) == 126:
				os.system("chmod +x mangohud-setup.sh")
				os.system("./mangohud-setup.sh install")
			if os.path.isfile("/usr/bin/mangohud"):
				print(colored.green("MangoHUD installed succesfully"))
				
	else:
		print("Cannot download MangoHud or can't locate it")
	if os.path.isfile("/usr/bin/goverlay"):
		print(colored.green("GOverlay already installed, updating GOverlay..."))
		os.rm("/usr/bin/goverlay")
		if os.path.exists("./GOverlay"):
			os.system("rm -rf ./GOverlay")
			os.mkdir("GOverlay")
	else:
		print(colored.green("Installing GOverlay..."))
		os.system("mkdir GOverlay")
	os.chdir("./GOverlay")

	goverlayTarball = downloadTarball("benjamimgois","goverlay",0)
	if os.path.isfile(goverlayTarball.split()[0]):
		if os.WEXITSTATUS(os.system("tar -xf {}".format(goverlayTarball))) == 2:
			sys.exit("Fatal error trying to extract the tarball")
		else:
			os.system("chmod +x goverlay")
			if os.WEXITSTATUS(os.system("mv goverlay /usr/bin/")) >0:
				print("Error trying to move goverlay file to /us/bin/ executing command as root...")
				os.system("sudo mv goverlay /usr/bin/")

			if os.path.isfile("/usr/bin/goverlay"):
				print(colored.green("GOverlay installed succesfully"))
			else:
				print("goverlay cannot be moved on /usr/bin/, you still can execute it from the current directory")
	else:
		print("GOverlay download MangoHud or can't locate it")
	
def protonGE(dist):	
	home = os.popen("echo ~/").read()
	steamFolder = "{}.steam/root/compatibilitytools.d/".format(home.split("\n"))
	flatpakSteamFolder = "{}.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/".format(home.split("\n"))
	

	#FIXME: Optimize this another if hell
	if not os.path.exists("{}.steam/root/".format(home.split("\n"))) and  not os.path.exists("{}.var/app/com.valvesoftware.Steam/".format(home.split("\n"))):
		op = input(print("Steam needs to be installed for this, do you want to install Steam? [Y/N] -> "))
		if op in CONFIRM:
			Steam(dist)
			print("It is needed to open Steam one time for create the folders, opening steam...")
			os.system("steam")
			protonGE(dist)
		elif op in DENY:
			print(colored.red("Installation cancelled"))
		else:
			print("Wrong option!")
	elif os.path.exists("{}.steam/root/".format(home.split("\n"))):
		print(colored.green("Detected steam installation folder on ~/.steam/"))
		if os.path.exists(steamFolder):
			print(colored.green("compatibilitytools.d folder detected under ~/.steam/root/"))
		else:
			if os.WEXITSTATUS(os.system("mkdir ~/.steam/root/compatibilitytools.d/")) == 126:
				print(colored.red("Cannot create the folder ~/.steam/root/compatibilitytools.d/, trying with sudo permissions..."))
				os.system("sudo mkdir ~/.steam/root/compatibilitytools.d/")
		os.chdir(steamFolder)
	elif os.path.exists("{}.var/app/com.valvesoftware.Steam/".format(home.split("\n"))):
		print(colored.green("Detected flatpak steam installation folder on ~/.var/app/com.valvesoftware.Steam/"))
		if os.path.exists(flatpakSteamFolder):
			print.colored.green("compatibilitytools.d folder detected under ~/.var/app/com.valvesoftware.Steam/data/Steam/")
		else:
			if os.WEXITSTATUS(os.system("mkdir ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/")) == 126:
				print(colored.red("Cannot create the folder ~/.steam/root/compatibilitytools.d/, trying with sudo permissions..."))
				os.system("sudo mkdir ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/")

		os.chdir(flatpakSteamFolder)
	
	protonGeTarball = downloadTarball("GloriousEggroll","proton-ge-custom",0)
	if os.WEXITSTATUS(os.system("tar -xf {}".format(protonGeTarball))) != 0:
		sys.exit(colored.red("Cannot extract the tarball"))	
	else:
		print(colored.green("Tarball extracted succesfully, ProtonGE is now installed, for enable it on Steam, see: https://github.com/GloriousEggroll/proton-ge-custom/#enabling"))
		os.rm(protonGeTarball)
		
def downloadTarball(username,repository,index):
	# Download the latest releas tarball and return the name of it.
	# FIXME: Handle errors from curl
	tarball = os.popen("curl -sL https://api.github.com/repos/{}/{}/releases/latest | jq -r '.assets[{}].browser_download_url'".format(username,repository,index)).read()
	os.system("wget {}".format(tarball))
	return tarball.split("/")[8]

def Steam(dist):
	if dist == "arch":
		os.system("sudo python3 enableMultilib.py program")
		os.system("sudo pacman -S steam --needed")
	elif dist == "ubuntu":
		os.system("sudo apt install steam-installer")
	else:
		print(colored.red("This shouldn't happen"))

def feralGamemode(dist):
	if dist == "arch":
		os.system("sudo pacman -S meson systemd git dbus")
		cloneFeralGamemode("arch")
	elif dist == "ubuntu":
		os.system("sudo apt install meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev libinih-dev")
		cloneFeralGamemode("ubuntu")
	else:
		print("wrong distro")


def Git(dist):
	if dist == "arch":
		os.system("sudo pacman -S git")
	elif dist == "ubuntu":
		os.system("sudo apt update")
		os.system("sudo apt install git")
	else:
		print(colored.red("wrong distro"))

def cloneFeralGamemode(dist):
		if os.path.exists("./Gamemode"):
			os.chdir("./Gamemode")
		else:
			os.system("mkdir Gamemode")
			os.chdir("./Gamemode")
		if os.WEXITSTATUS(os.system("git clone https://github.com/FeralInteractive/gamemode.git")) == 127:
			git = input(print(colored.red("Cannot found Git, Git is needed for install some programs, proceed to install Git? [Y/N]")))
			if git == "y" or git == "Y":
				Git(dist)
				os.system("git clone https://github.com/FeralInteractive/gamemode.git")
			elif git == "n" or git == "N":
				sys.exit("Installation cancelled")
		os.chdir("gamemode")
		os.system("git checkout 1.5.1")
		os.system("sudo chmod +x bootstrap.sh")
		os.system("./bootstrap.sh")

