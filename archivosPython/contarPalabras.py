# funcion que cuenta las palabras de un texto sin usar la funcion split
def contarPalabras(texto):
    texto = texto.replace(",", " ")
    texto = texto.replace(".", " ")
    texto = texto.replace(";", " ")
    texto += " "
    palabras = []
    inicio = 0
    while True:
        if texto[inicio] == ' ':
            inicio += 1
        else:
            fin = inicio + 1
            while texto[fin] != ' ':
                fin += 1
            palabras.append(texto[inicio:fin])
            inicio = fin + 1
        if inicio >= len(texto):
            break
    return palabras

# llama a la funcion
texto = 'Ingrese un texto:'
print(contarPalabras(texto))