#Ejercicios de Funciones 2
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

# se define el espacio para que el mensaje se escriba junto a los nombres
def salud_persiona(nombre):
    # se imprime el mensaje junto a los nombres
    print("!Hola,", nombre,"¡")
# se establecen los nomnbres especificados 
salud_persiona("Miguel")
salud_persiona("Jeremias")
salud_persiona("Jose")