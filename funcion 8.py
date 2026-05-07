#Ejercicios de Funciones 3
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

import math

# define el valor y llama a la operacion desde el math para hacer calcular el factorial
def factorial(a):
    return math.factorial(a)
total = factorial(10)
print(f"El factorial {total} .")
