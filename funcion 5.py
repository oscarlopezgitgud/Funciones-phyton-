#Funciones EJEMPLOS PRÁCTICOS 4
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

def datos_persona(nombre, edad):
    return nombre, edad
n, e = datos_persona("Carlos", 20)
print("Nombre:", n, "Edad:", e)