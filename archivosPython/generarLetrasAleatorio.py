# funcion que genera una lista de letras aleatorias
def generarLetrasAleatorio(n):
    from random import randint
    letras = []
    for i in range(n):
        letras.append(chr(randint(97, 122)))
    return letras

#llamamos a la funcion
#print(generarLetrasAleatorio(10))

# generar una lista de simbolos aleatorios
def generarSimbolosAleatorio(n):
    from random import randint
    simbolos = []
    for i in range(n):
        simbolos.append(chr(randint(33, 47)))
    return simbolos

#llamamos a la funcion
#print(generarSimbolosAleatorio(10))

# generar una lista de letras mayusculas aleatorios
def generarLetrasMayusculasAleatorio(n):
    from random import randint
    letras = []
    for i in range(n):
        letras.append(chr(randint(65, 90)))
    return letras

#llamamos a la funcion
#print(generarLetrasMayusculasAleatorio(10))

# generar una lista de letras mayusculas y minusculas y simbolos aleatorios
def generarLetrasMayusculasMinusculasSimbolosAleatorio(n):
    from random import randint
    string = []
    for i in range(n):
        #variable de control 
        control = randint(0, 2)
        #condicional para que las letras mayusculas y minusculas y simbolos sean aleatorios
        if control == 0:
            #letras mayusculas
            string.append(generarLetrasMayusculasAleatorio(1))
        elif control == 1:
            #letras minusculas
            string.append(generarLetrasAleatorio(1))
        else:
            #simbolos
            string.append(generarSimbolosAleatorio(1))
    return string

#llamamos a la funcion
#print(generarLetrasMayusculasMinusculasSimbolosAleatorio(10))

#generar una lista de numeros aleatorios
def generarNumerosAleatorio(n, min, max):
    from random import randint
    numeros = []
    for i in range(n):
        numeros.append(randint(min, max))
    return numeros

#llamamos a la funcion
#print(generarNumerosAleatorio(10, 100, 200))

# comprobar si una operacion hecha por el usuario es correcta
def comprobarOperacion(respuesta, resultado):
    # buscar luego: eval()
    if respuesta == resultado:
        return True
    else:
        return False

#generar una operacion matematica aleatoria
def generarOperacionAleatoria():
    from random import randint
    #variable de control
    control = randint(1, 4)
    #numeros aleatorios, llamamos a la funcion
    numero1 = int(generarNumerosAleatorio(2, 1, 10)[0])
    numero2 = int(generarNumerosAleatorio(2, 1, 10)[0])
    #condicional para que las operaciones sean aleatorias
    if control == 1:
        #suma
        print(numero1, "+", numero2)
        respuesta = int(input("Respuesta: "))
        resultado = numero1 + numero2
    elif control == 2:
        #resta
        print(numero1, "-", numero2)
        respuesta = int(input("Respuesta: "))
        resultado = numero1 - numero2
    elif control == 3:
        #multiplicacion
        print(numero1, "*", numero2)
        respuesta = int(input("Respuesta: "))
        resultado = numero1 * numero2
    else:
        #division
        print(numero1, "/", numero2)
        respuesta = float(input("Respuesta: "))
        resultado = numero1 / numero2
    #comprobamos si la respuesta es correcta
    if comprobarOperacion(respuesta, resultado):
        print("Correcto") 
    else:
        print("Incorrecto")
    
#llamamos a la funcion while 5 veces
if __name__=="main":
    control = 0
    while control < 6:
        print(generarSimbolosAleatorio(10))
        control += 1
        #linea de separacion
        print("-" * 50)   