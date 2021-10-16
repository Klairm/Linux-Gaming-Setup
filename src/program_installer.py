from clint.textui import colored

RED = colored.red
GREEN = colored.green


class ProgramInstaller:
    def __init__(self, factory):
        self.factory = factory

    def install(self):
        while True:
            print(GREEN(
                "\n[1] WINE (Essential)\n[2] Lutris\n[3] GOverlay with MangoHUD\n[4] Steam\n[5] Feral GameMode\n[6] Proton GE\n[7] Lutris GE\n[8] Heroic Games Launcher\n[0] Back"))
            program = int(input("Select an option -> "))
            if program == 1:
                self.factory.wine_installer().install()
            elif program == 2:
                self.factory.lutris_installer().install()
            elif program == 3:
                self.factory.g_overlay_with_mango_installer().install()
            elif program == 4:
                self.factory.steam_installer().install()
            elif program == 5:
                self.factory.feral_game_mode_installer().install()
            elif program == 6:
                self.factory.proton_ge_installer().install()
            elif program == 7:
                self.factory.lutris_ge_installer().install()

            elif program == 8:
                self.factory.heroic_games_installer().install()
            elif program == 0:
                break

            else:
                print(RED("Wrong option!"))
