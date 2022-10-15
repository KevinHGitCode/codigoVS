# lista de * con un espacio por indice
A=[(" "*i)+"*" for i in range(10)]
print(A)

#funcion recorerr una lista e imprimir
def imprimir(lista):
    for i in lista:
        print(i)

#recorrer una lista e imprimir en reversa
def imprimir_reversa(lista):
    for i in lista[::-1]:
        print(i)

#funcion borrar pantalla
def borrar_pantalla():
    print("\n"*100)

#funcion esperar
def esperar():
    input("\nPresione enter para continuar ")
    return True

#while 10 veces
# variable contador
contador=0
while contador<10:
    #funcion imprimir
    imprimir(A)
    #funcion imprimir reversa
    imprimir_reversa(A)
    #preguntar si quiere borrar pantalla
    #si quiere borrar pantalla
    if esperar():
        #funcion borrar pantalla
        borrar_pantalla()