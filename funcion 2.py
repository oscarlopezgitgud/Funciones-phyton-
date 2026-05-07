#Funciones EJEMPLOS PRÁCTICOS 1
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

def saludar():
    print("Hola... Bienvenido")

saludar()
saludar()
