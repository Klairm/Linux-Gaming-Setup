from src.utils.apt import Apt
from src.debian.driver_installer import DriverInstaller
from src.debian.feral_game_mode_installer import FeralGameModeInstaller
from src.debian.g_overlay_with_mango_installer import GOverlayWithMangoInstaller
from src.debian.git_installer import GitInstaller
from src.debian.lutris_installer import LutrisInstaller
from src.program_installer import ProgramInstaller
from src.utils.proton_ge_installer import ProtonGeInstaller
from src.debian.steam_installer import SteamInstaller
from src.debian.wine_installer import WineInstaller
from src.debian.heroic_games_installer import HeroicGamesInstaller


class Factory:
    def __init__(self):
        self.apt = Apt()

    def driver_installer(self):
        return DriverInstaller(apt=self.apt)

    def feral_game_mode_installer(self):
        return FeralGameModeInstaller(apt=self.apt, factory=self)

    def g_overlay_with_mango_installer(self):
        return GOverlayWithMangoInstaller(apt=self.apt)

    def git_installer(self):
        return GitInstaller(apt=self.apt)

    def lutris_installer(self):
        return LutrisInstaller(apt=self.apt)

    def program_installer(self):
        return ProgramInstaller(factory=self)

    def proton_ge_installer(self):
        return ProtonGeInstaller(factory=self)

    def steam_installer(self):
        return SteamInstaller(apt=self.apt)

    def wine_installer(self):
        return WineInstaller(apt=self.apt)

    def heroic_games_installer(self):
        return HeroicGamesInstaller()
