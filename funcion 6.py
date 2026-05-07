#Ejercicios de Funciones 1
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

# Define los valores a imprimir y los guarde entro de la definicion
def saludo():
    print("Hola amigo/a/e")
# Llaman la definicion para que se imprima 
saludo()
saludo()
saludo()