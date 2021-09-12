from src.ubuntu.driver_installer import DriverInstaller
from src.ubuntu.feral_game_mode_installer import FeralGameModeInstaller
from src.ubuntu.g_overlay_with_mango_installer import GOverlayWithMangoInstaller
from src.ubuntu.git_installer import GitInstaller
from src.ubuntu.lutris_installer import LutrisInstaller
from src.program_installer import ProgramInstaller
from src.proton_ge_installer import ProtonGeInstaller
from src.ubuntu.steam_installer import SteamInstaller
from src.ubuntu.wine_installer import WineInstaller


class Factory:
    def driver_installer(self):
        return DriverInstaller()

    def feral_game_mode_installer(self):
        return FeralGameModeInstaller(self)

    def g_overlay_with_mango_installer(self):
        return GOverlayWithMangoInstaller()

    def git_installer(self):
        return GitInstaller()

    def lutris_installer(self):
        return LutrisInstaller()

    def program_installer(self):
        return ProgramInstaller(self)

    def proton_ge_installer(self):
        return ProtonGeInstaller(self)

    def steam_installer(self):
        return SteamInstaller()

    def wine_installer(self):
        return WineInstaller()
