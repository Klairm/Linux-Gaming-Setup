class GitInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        self.apt.install(["git"])
