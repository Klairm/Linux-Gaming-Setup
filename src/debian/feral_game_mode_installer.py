from src.feral_game_mode_installer import FeralGameModeInstaller as Base


class FeralGameModeInstaller(Base):
    def __init__(self, factory, apt):
        super().__init__(factory=factory)
        self.apt = apt

    def install(self):
        self.apt.install(["meson", "libsystemd-dev", "pkg-config", "ninja-build", "git", "libdbus-1-dev", "libinih-dev"])
        self.clone_feral_game_mode()
