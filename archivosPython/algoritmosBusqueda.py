# crea la funcion busquedaBinaria
def busquedaBinaria(lista, elemento):
    # inicializamos los valores de inicio y fin
    inicio = 0
    fin = len(lista) - 1
    # mientras el inicio sea menor o igual al fin
    while inicio <= fin:
        # calculamos el valor medio de la lista
        medio = (inicio + fin) // 2
        # si el elemento es igual al medio
        if lista[medio] == elemento:
            # retornamos el medio
            return medio
        # si el elemento es menor al medio
        elif lista[medio] < elemento:
            # cambiamos el inicio a el medio + 1
            inicio = medio + 1
        # si el elemento es mayor al medio
        else:
            # cambiamos el fin a el medio - 1
            fin = medio - 1
    # si no se encontro el elemento
    return -1

#llamamos la funcion
#print(busquedaBinaria([1,2,3,4,5,6,7,8,9,10], 5))

# crea la funcion estaOrdenada
def estaOrdenada(lista):
    # inicializamos el valor de inicio
    inicio = 0
    # mientras el inicio sea menor que el fin
    while inicio < len(lista) - 1:
        # si el elemento es mayor al siguiente
        if lista[inicio] > lista[inicio + 1]:
            # retornamos False
            return False
        # si no
        else:
            # cambiamos el inicio a el inicio + 1
            inicio += 1
    # si no se cumple la condicion
    return True

# llamamos la funcion
#print(estaOrdenada([1,2,3,4,5,6,7,8,9,10]))

#busqueda binaria contar comparaciones
def busquedaBinariaContarComparaciones(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    contadorComparaciones=0
    while inicio <= fin:
        medio = (inicio + fin) // 2
        print(medio)
        contadorComparaciones+=1
        if lista[medio] == elemento:
            print("Comparaciones: ", contadorComparaciones)
            return medio, contadorComparaciones
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1, contadorComparaciones

#lista aleatoria 100 elementos
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
#elemento a buscar

comparaciones=[]
for i in lista:
    posicion, contadorComparaciones = busquedaBinariaContarComparaciones(lista, i)
    print("se encontro en la posicion:", posicion)
    print("-----------------------------------------------------")
    comparaciones.append(contadorComparaciones)

print("el promedio de comparaciones es:",sum(comparaciones)/len(comparaciones))

#ordenar comparaciones
comparaciones.sort()
#print la mmediana de comparaciones
print("la mediana de comparaciones es:",comparaciones[len(comparaciones)//2])

#diccionario de comparaciones
diccionarioComparaciones={}
for i in comparaciones:
    #si i no esta en el diccionario lo agrega con el valor 1
    if i not in diccionarioComparaciones:
        diccionarioComparaciones[i]=1
    #si i esta en el diccionario lo suma 1
    else:
        diccionarioComparaciones[i]+=1

print("el diccionario de comparaciones es:",diccionarioComparaciones)