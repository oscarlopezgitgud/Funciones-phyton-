#Funciones EJEMPLOS PRÁCTICOS 3
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

# se definen los primeros 2 valores a usar
def sumar(a, b):
    # se establecen las operaciones a hacer
    return a + b
    # se aplican los valores a la operacion
resultado = sumar(5, 3)
#se escribe el mensaje con el resultado de la definicion
print("La suma es:", resultado)
