#funcion ordenamiento por insercion | insertion sort
def ordInsercion(lista):
    for i in range(1,len(lista)):
        j=i
        while j>0 and lista[j-1]>lista[j]:
            lista[j-1],lista[j]=lista[j],lista[j-1]
            j-=1
    return lista

#funcion ordenamiento por seleccion | selection sort
def ordSeleccion(lista):
    for i in range(len(lista)):
        indice=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[indice]:
                indice=j
        lista[i],lista[indice]=lista[indice],lista[i]
    return lista

#funcion ordenamiento por burbuja | bubble sort
def ordBurbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
    '''
    O tambien:
    
    def metodoBurbuja(lista):
        aux=0
        aux2=0
        for i in range(len(lista)-1):
            for j in range(len(lista)-1):
                if lista[j]>lista[j+1]:
                    aux=lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=aux
            #print(lista)     
        return lista
    '''

#funcion ordenamiento por burbuja bidireccional | Cocktail sort
def ordBurbujaBidireccional(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
            if lista[j]<lista[j-1]:
                lista[j],lista[j-1]=lista[j-1],lista[j]
    return lista

#funcion ordenamiento por ordenamiento de peine | Comb sort
def ordPeine(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

#funcion ordenamiento por shell | Shell sort 
def ordShell(lista):
    gap=len(lista)//2
    while gap>0:
        for i in range(gap,len(lista)):
            j=i
            while j>=gap and lista[j-gap]>lista[j]:
                lista[j-gap],lista[j]=lista[j],lista[j-gap]
                j-=gap
        gap//=2
    return lista

#funcion ordenamiento batcher | Batcher odd-even mergesort / Bitonic sort
def ordBatcher(lista):
    for i in range(len(lista)//2):
        for j in range(i,len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

#funcion ordenamiento rapido | Quicksort
def ordRapido(lista):
    if len(lista)<=1:
        return lista
    pivote=lista[0]
    izq=[]
    der=[]
    for i in range(1,len(lista)):
        if lista[i]<pivote:
            izq.append(lista[i])
        else:
            der.append(lista[i])
    return ordRapido(izq)+[pivote]+ordRapido(der)