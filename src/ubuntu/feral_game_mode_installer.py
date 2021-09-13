from src.debian.feral_game_mode_installer import FeralGameModeInstaller as Base
import distro


class FeralGameModeInstaller():
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        if int(distro.major_version()) >= 19:
            self.apt.install(["gamemode"])
        elif int(distro.major_version() <= 18):
            pass
