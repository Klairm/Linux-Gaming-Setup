# Linux-Gaming-Setup
A python script which allow users to install drivers and programs of utility and be able to play games on Linux

- Drivers installer based on Lutris wiki https://github.com/lutris/lutris/wiki/Installing-drivers

With this script you can currently install drivers for Debian, Ubuntu and Arch, more distros will be added
You can install this programs:
	
	- WINE: A program that allows execute Windows programs on Linux, for more info you can visit https://www.winehq.org/
	
	- Lutris: A gaming client for Linux, which allows you to install games and emulators without too much tweaking, you can visit https://lutris.net/about/ for more info

	- Steam: A platform for buy and install games, also you can chat with your friends, install and share mods on the workshop and it has more features https://store.steampowered.com/about/
	
	- GOverlay: It's an GUI for manage Linux overlays, such as MangoHUD. https://github.com/benjamimgois/goverlay

	- MangoHUD: A Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU loads and more. https://github.com/flightlessmango/MangoHud

More will be added in a future


# Usage ( for now ):
- Give execution rights to setup.sh and execute it in order to install the dependencies
```chmod +x setup.sh```
- Execute the script and select your distro or distro-based
```./setup.sh```
- Now you can execute the python script
``` python3 GamingSetup.py ```  or alternative ```./GamingSetup.py``` 



# TO DO
- Finish the project, ie: adding possible fedora support, Debian drivers installation,add more useful and essential programs...
- Create error handler , for basics and common errors, as TypeError, etc...
- Provide as an distributable file, ie: providing a way for install python dependencies automatically
- Create a GUI version
- Create a bash version so no need to download any dependencies

# GUI Version

In the repo of Forknife , it's where the GUI version is being worked on https://github.com/RubixPower/Linux-Gaming-Setup
He made all the job on that version, and it's more easy to use, also cleaner code
