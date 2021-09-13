from clint.textui import colored


class DriverInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        print(colored.red("FIXME: Add drivers installer for Debian"))
