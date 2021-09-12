import os

from src.feral_game_mode_installer import FeralGameModeInstaller as Base


class FeralGameModeInstaller(Base):
    def install(self):
        os.system("sudo pacman -S meson systemd git dbus")
        self.clone_feral_game_mode()
