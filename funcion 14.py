#Ejercicios de Funciones 9
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

import math

# define los 2 valores para calcular el mcd
def mcmd(a,b):
    # regresa los valores junto a la operacion importada
    return  math.gcd(a,b)
    # aplica los valores para operar
resultado = mcmd(10,5)
#imprime el resultado de los valores calculados 
print(f"El MCD es :{resultado}")

# define los 2 valores para calcular el mcm
def mcm(a,b):
     # regresa los valores junto a la operacion importada
    return math.lcm(a,b)
    # aplica los valores para operar
resultado = mcm(10,5)
#imprime el resultado de los valores calculados 
print(f"El MCM es :{resultado}")