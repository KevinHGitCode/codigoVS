#importar colorama
import math
from colorama import init, Fore, Back, Style

#funcion que recibe un texto y un color, y con un match() case: para selecionar 5 opciones de color.
def colorTexto(texto, color):
    # match
    match(color):
        case 'rojo':
            print(Fore.RED + texto)
        case 'azul':
            print(Fore.BLUE + texto)
        case 'verde':
            print(Fore.GREEN + texto)
        case 'amarillo':
            print(Fore.YELLOW + texto)
        case 'magenta':
            print(Fore.MAGENTA + texto)
        case 'cyan':
            print(Fore.CYAN + texto)
        case 'blanco':
            print(Fore.WHITE + texto)
        case _:
            #color negro
            print(Fore.BLACK + texto)

#TODO: funcion print bold

#call the function
colorTexto('Hello World!', input('elige el color: '))