#Ejercicios de Funciones 10
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

# se define el valor decimal junto a su operacion en para transformar en binario 
def decabin(decimal):
    return bin(decimal)
# imprime el valor traducido a binario 
binariodec = decabin(13)
print(f"El numero traducido a binario es {binariodec}")

# se define el valor binario junto a su operacion en para transformar en decimal
def binadec(binario):
    return int(binadec, 2)
# imprime el valor traducido a decimal
decimalbin = binadec('101')
print("El numero traducido a binario es ", decimalbin )