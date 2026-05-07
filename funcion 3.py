#Funciones EJEMPLOS PRÁCTICOS 2
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

def saludar_persona(nombre):
    print("¡Hola, ", nombre, "!")
saludar_persona("Ana")
saludar_persona("Luis")