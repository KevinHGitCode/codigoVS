#funcion limpiarConsola
def limpiarConsola():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#imprimimos el mensaje de bienvenida
print("Bienvenido al programa de limpieza de la consola")

#limpiamos la consola
input("Pulse enter para limpiar la consola")
limpiarConsola()