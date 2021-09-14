from src.utils.feral_game_mode_installer import FeralGameModeInstaller as Base
import distro


class FeralGameModeInstaller(Base):
    def __init__(self, factory, apt):
        super().__init__(factory=factory)
        self.apt = apt

    def install(self):
        if int(distro.major_version()) >= 19 and distro.id() == "ubuntu":
            self.apt.install(["gamemode"])
        else:
            # Workaround for https://github.com/mesonbuild/meson/issues/6997
            if distro.id() == "ubuntu":
                self.apt.install(["software-properties-common"])
                self.apt.add_repository("ppa:team-xbmc/ppa")
                self.apt.update()

            self.apt.install(["meson", "libsystemd-dev", "pkg-config",
                             "ninja-build", "git", "libdbus-1-dev", "libinih-dev", ])
            self.clone_feral_game_mode()
