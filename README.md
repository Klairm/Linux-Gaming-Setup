## Linux-Gaming-Setup

A python script which allow users to install drivers and programs of utility to play games on Linux

Drivers installation based on [Lutris wiki](https://github.com/lutris/docs/blob/master/InstallingDrivers.md)

With this script you can currently install drivers for Debian, Ubuntu and Arch, more distros will be added
You can install this programs:
| Program | Description |
| ------- | ----------- |
| [WINE](https://www.winehq.org/) | A program that allows execute Windows programs on Linux |
| [Lutris](https://github.com/lutris/lutris) | A gaming client for Linux, which allows you to install games and emulators without too much tweaking, you canvisit https://lutris.net/about/ for more info |
| [Steam](https://store.steampowered.com/about/) | A platform for buy and install games, also you can chat with your friends, install and share mods on the workshop and it has more features |
| [GOverlay](https://github.com/benjamimgois/goverlay) | It's an GUI for manage Linux overlays, such as MangoHUD |
| [MangoHUD](https://github.com/flightlessmango/MangoHud) | A Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU loads and more |
| [Feral Gamemode](https://github.com/FeralInteractive/gamemode) | A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS and/or a game process |
| [ProtonGE](https://github.com/GloriousEggroll/proton-ge-custom/) | A custom build from Proton with some fixes for games. |
| [WineGE/LutrisGE](https://github.com/GloriousEggroll/wine-ge-custom) | A custom build from Wine with some fixes for games made to use with Lutris. |
| [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | A Native GUI Epic Games Launcher for Linux, Windows and Mac. |

More will be added in a future

## Setup:

1. Give execution rights to `setup.sh` and execute it in order to install the dependencies:
   `chmod +x setup.sh`
2. Execute the script and select your distro or distro-based
   `./setup.sh`
3. Now you can execute the python script
   `./GamingSetup.py` or alternative `python3 GamingSetup.py`

### GUI Version

GUI version is in the task list [#17](https://github.com/Klairm/Linux-Gaming-Setup/issues/17) but Forknife already made one and can be found [here](https://github.com/RubixPower/Linux-Gaming-Setup)
