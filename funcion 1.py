#Funciones en python, ejercicio de Prueba
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

def saludar():
    print("Hola, Bienvenidos a funciones en phyton")
saludar()