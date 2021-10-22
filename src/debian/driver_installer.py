from clint.textui import colored

RED = colored.red


class DriverInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        print(RED("FIXME: Add drivers installer for Debian"))
