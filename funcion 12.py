#Ejercicios de Funciones 7
#Oscar Daniel Alejandro Lopez Ramirez

import pyfiglet
from colorama import init, Fore, Back, Style
init()
titulo = pyfiglet.figlet_format("Oscar")
print(Fore.BLUE + titulo + Style.RESET_ALL)

#establece multiples valores para poder calcular sus cuadrados
def cuadrados(nu1,nu2,nu3,nu4,nu5):
    # Se establecen las operaciones (potencias) de cada uno de los valores 
    return nu1**2,nu2**2,nu3**2,nu4**2,nu5**2
    #Se imprime el resultado de todas las operaciones junto a sus valores a calcular 
print(f"Los cuadrados son:{cuadrados(10,5,2,4,2)}")
