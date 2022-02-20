from clint.textui import colored
GREEN = colored.green 

class LutrisInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        print(GREEN("Adding lutris repository"))
        self.apt.add_repository("ppa:lutris-team/lutris")
        self.apt.install(["lutris"])
