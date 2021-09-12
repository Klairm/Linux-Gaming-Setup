import os

from src.feral_game_mode_installer import FeralGameModeInstaller as Base


class FeralGameModeInstaller(Base):
    def install(self):
        os.system("sudo apt install meson libsystemd-dev pkg-config ninja-build git libdbus-1-dev libinih-dev")
        self.clone_feral_game_mode()

