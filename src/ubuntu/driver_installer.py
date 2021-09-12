from clint.textui import colored
import distro


class DriverInstaller:
    def __init__(self, apt):
        self.apt = apt

    def install(self):
        while True:
            print(colored.red("WARNING: Choose your correct brand of your graphics card"))
            print(colored.green("\n[1] NVIDIA\n[2] AMD/INTEL\n[3] Back\n"))
            brand = int(input("Select an option -> "))

            if brand == 1:
                print(colored.red('''
                WARNING: Make sure that your graphics card is compatible with the driver and is Vulkan capable, before installing: 

                Graphics card compatibility -> https://www.nvidia.com/Download/driverResults.aspx/157462/en-us

                Check if your GPU it's Vulkan capable -> https://en.wikipedia.org/wiki/Vulkan_(API)#Compatibility '''))
                op = input("Do you want to continue? [Y/N] ->  ")

                if op == 'Y' or op == 'y':
                    print(colored.red("Adding drivers repository and enabling 32 bits arch "))
                    self.apt.add_architecture("i386")
                    self.apt.add_repository("ppa:graphics-drivers/ppa")

                    print(colored.green("Installing the 440 driver"))
                    self.apt.install(["nvidia-driver-440", "libnvidia-gl-440", "libnvidia-gl-440:i386"])

                    print("Reboot to apply changes")
                elif op == 'N' or op == 'n':
                    break
                else:
                    print("Wrong option, select Y or N")

            elif brand == 2:
                print(colored.red('''
                    Note: Only Ubuntu 18.04 and higher is supported for AMD and Intel graphics.
            
                    Note for Intel integrated graphics users: Only Skylake, Kaby Lake, and Coffee Lake offer full Vulkan support. 
                    Broadwell, Haswell and Ivy Bridge only offer partial support, which may not work with a lot of games. 
                    Sandy Bridge and older lack any Vulkan support whatsoever.
            
                    Check if your GPU it's Vulkan capable -> https://en.wikipedia.org/wiki/Vulkan_(API)#Compatibility
                    '''))

                op = input("Do you want to continue? [Y/N] ->  ")

                if op == 'Y' or op == 'y':
                    ver = distro.linux_distribution()[1]

                    if float(ver) >= 19.10:
                        print(colored.green(
                            f"Detected {ver[0]} {ver[1]}, installing support for 32 bit and vulkan support"))
                        self.apt.add_architecture("i386")
                        self.apt.install(["libgl1-mesa-dri:i386", "mesa-vulkan-drivers", "mesa-vulkan-drivers:i386"])

                        print("Reboot to apply changes")
                    elif float(ver) == 18.04 or float(ver) == 18.10:
                        print(colored.green(
                            f"Detected {ver[0]} {ver[1]}, adding mesa repository, installing support for 32 bit and vulkan support"))
                        self.apt.add_architecture("i386")
                        self.apt.add_repository("ppa:kisak/kisak-mesa")
                        self.apt.upgrade()
                        self.apt.install(["libgl1-mesa-glx:i386", "libgl1-mesa-dri:i386", "mesa-vulkan-drivers", "mesa-vulkan-drivers:i386"])

                        print("Reboot to apply changes")
                    elif float(ver) < 18.04:
                        print(colored.red("Only Ubuntu 18.04 and higher is supported for AMD and Intel graphics."))
                        break
                    else:
                        print("Something went wrong")  # FIXME: Add error handler

            elif brand == 3:
                break

            else:
                print("Wrong option, you must choose one number")

