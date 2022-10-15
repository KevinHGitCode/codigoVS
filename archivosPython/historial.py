# crear un historial con pila

# crear pila
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        return self.items.pop()

    def es_vacia(self):
        return self.items == []

    def __str__(self):
        return str(self.items)

    #mostrar historial
    def mostrar_historial(self):
        return self.items

#insertar elementos en la pila
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
pila.apilar(6)

print(pila.mostrar_historial())

# match de 4 opciones
# contador
contador = 0
retro=[]
#while 
while contador < 4:
    print("navegando historial\n"+"-"*20)
    print("1. retroceder")
    print("2. avanzar")
    print("3. mostrar historial")
    print("4. salir")
    op=int(input("ingrese opcion: "))
    match(op):
        case 1:
            retro.append(pila.items[-1])
            pila.desapilar()
            print(pila.mostrar_historial())
        case 2:
            if retro != []:
                pila.apilar(retro[-1])
                retro.pop(-1)
            print(pila.mostrar_historial())
        case 3:
            print(pila.mostrar_historial())
        case 4:
            print("salir")
            break
        case _:
            print("no es una opcion")