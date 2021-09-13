import os


class Apt:
    def __init__(self):
        self.needs_update = True

    def install(self, packages, recommends=False):
        self.update()

        options = []

        if recommends:
            options.append("--install-recommends")

        command = "sudo apt install"
        option_list = " ".join(options)
        package_list = " ".join(packages)

        os.system(" ".join([command, option_list, package_list]))

    def update(self, force=False):
        if force or self.needs_update:
            os.system("sudo apt-get update")
            self.needs_update = False

    def upgrade(self):
        self.update()
        os.system("sudo apt-get upgrade")

    def add_architecture(self, architecture):
        os.system("sudo dpkg --add-architecture " + architecture)
        self.needs_update = True

    def add_key(self, key):
        os.system("sudo apt-key add " + key)

    def add_repository(self, repository):
        os.system("sudo add-apt-repository " + repository)
        self.needs_update = True
