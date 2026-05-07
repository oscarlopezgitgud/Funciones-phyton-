#Ejercicios de Funciones 6
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

import statistics

def calcular_media(datos):
    if not datos: 
        return 0
    return sum(datos) / len(datos)

numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(numeros)
print(f"La media es: {resultado}") # Resultado: 30.0
Ejemplos y detalles clave: