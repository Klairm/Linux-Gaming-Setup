import os

from clint.textui import colored


def brandSelArch():
	while True:
		print(colored.red("WARNING: Choose your correct brand of your graphics card"))
		print(colored.green("\n[1] NVIDIA\n[2] AMD\n [3] INTEL\n[4] Back\n"))
		brArchnd = int(input("Select an option -> "))

		if brArchnd == 1:
			print(colored.red('''
				Warning: Please ensure your graphics card is supported by modern Nvidia driver before installing. For a list of supported GPUs click here:
				https://www.nvidia.com/Download/driverResults.aspx/157462/en-us

				Propietary drivers for Nvidia and Vulkan support will be installed now.

				'''))
			os.system("sudo pacman -S nvidia nvidia-utils lib32-nvidia-utils nvidia-settings vulkan-icd-loader lib32-vulkan-icd-loader --needed")
		elif brArchnd == 2:
			print(colored.red('''
				Before installing, Check if your GPU it's Vulkan capable -> https://en.wikipedia.org/wiki/Vulkan_(API)#Compatibility 
				'''))
			op = input("Do you want to continue? [Y/N] -> ")
			if op == 'Y' or op == 'y':
				os.system("sudo pacman -S lib32-mesa vulkan-radeon lib32-vulkan-radeon vulkan-icd-loader lib32-vulkan-icd-loader --needed")
			elif op == 'N' or op == 'n':
				break
			else:
				print("Wrong option")
				break

		elif brArchnd == 3:
			print(colored.red('''
				Before installing, Check if your GPU it's Vulkan capable -> https://en.wikipedia.org/wiki/Vulkan_(API)#Compatibility 
				
				Note: Only Skylake, Kaby Lake, and Coffee Lake offer full Vulkan support. 
				Broadwell, Haswell and Ivy Bridge only offer partial support, which may not work with a lot of games. 
				Sandy Bridge and older lack any Vulkan support whatsoever.
				'''))

			op = input("Do you want to continue? [Y/N] -> ")

			if op == 'Y' or op == 'y':
				os.system("sudo pacman -S lib32-mesa vulkan-intel lib32-vulkan-intel vulkan-icd-loader lib32-vulkan-icd-loader --needed")
			elif op == 'N' or op == 'n':
				break
			else:
				print("Wrong option")
				break
		elif brArchnd == 4:
			break
