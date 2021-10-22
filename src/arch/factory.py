from src.arch.driver_installer import DriverInstaller
from src.arch.feral_game_mode_installer import FeralGameModeInstaller
from src.arch.g_overlay_with_mango_installer import GOverlayWithMangoInstaller
from src.arch.git_installer import GitInstaller
from src.arch.lutris_installer import LutrisInstaller
from src.program_installer import ProgramInstaller
from src.utils.proton_ge_installer import ProtonGeInstaller
from src.utils.lutris_ge_installer import LutrisGeInstaller
from src.arch.steam_installer import SteamInstaller
from src.arch.wine_installer import WineInstaller
from src.arch.yay_installer import YayInstaller
from src.arch.heroic_games_installer import HeroicGamesInstaller


class Factory:
    def driver_installer(self):
        return DriverInstaller()

    def feral_game_mode_installer(self):
        return FeralGameModeInstaller(self)

    def g_overlay_with_mango_installer(self):
        return GOverlayWithMangoInstaller(self)

    def git_installer(self):
        return GitInstaller()

    def lutris_installer(self):
        return LutrisInstaller()

    def program_installer(self):
        return ProgramInstaller(self)

    def proton_ge_installer(self):
        return ProtonGeInstaller(self)

    def lutris_ge_installer(self):
        return LutrisGeInstaller()

    def steam_installer(self):
        return SteamInstaller()

    def wine_installer(self):
        return WineInstaller()

    def yay_installer(self):
        return YayInstaller(self)

    def heroic_games_installer(self):
        return HeroicGamesInstaller(self)
