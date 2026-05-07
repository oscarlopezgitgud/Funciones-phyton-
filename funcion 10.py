#Ejercicios de Funciones 5
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

def area(pi, radio):
    return pi * radio**2
total_area = area(3.14, 5)
print(f"La area del circulo es: {total_area}")

def volumen(P,R,H):
    return P * R**2 * H
total_volumen = volumen(3.14,4,5)
print(f"El volumen del cilindro es: {total_volumen}")
