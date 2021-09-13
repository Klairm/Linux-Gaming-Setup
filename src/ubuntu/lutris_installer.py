from clint.textui import colored


class LutrisInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        print(colored.green("Adding lutris repository"))
        self.apt.add_repository("ppa:lutris-team/lutris")
        self.apt.install(["lutris"])
