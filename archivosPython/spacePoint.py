import generarLetrasAleatorio as ga
import esperarPorAccion as ea
    
lista=ga.generarNumerosAleatorio(max=40, min=0, n=1000)

print("la lista origenal es:",lista)

#print("la lista ordenada es:",metodoBurbuja(lista))

#genera una lista con * y espacios que dependen de un numero ejemplo: lista[1, 2, 3] => lista[ *,  *,   *] (un espacio *, dos espacios *, tres espacios *)
def spacePoint(var):
    # if type(var!=list):
    #     var=list(var)
    # a=(" "*j)+"*" for j in range(len(var))
    a=[]
    for i in var:
        a.append((" "*i)+"*")
    for i in a:
        ea.esperar(0.05)
        print(i)    

spacePoint(lista)