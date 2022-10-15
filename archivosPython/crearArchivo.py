#crear un archivo con el nombre que se le pase como argumento

#abrir en modo escritura ("w")
archivo = open("archivo2.pdf", "w")
archivo.write("Hola mundo")
archivo.close()

#TODO: trabajar mas con archivos

'''
#abrir en modo lectura ("w+")
archivo = open("archivo2.txt", "w+")
archivo.write("Hola mundo")
archivo.close()

#abrir en modo binario ("wb")
archivo = open("archivo2.txt", "wb")
archivo.write(b"Hola mundo")
archivo.close()

#abrir en modo binario ("wb+")
archivo = open("archivo2.txt", "wb+")
archivo.write(b"Hola mundo")
archivo.close()

#=====================================================#

#abrir en modo lectura ("r")
archivo = open("archivo2.txt", "r")
print(archivo.read())
archivo.close()

#abrir en modo lectura y escritura ("r+")
archivo = open("archivo2.txt", "r+")
print(archivo.read())
archivo.write("Hola mundo")
archivo.close()

#abrir en modo lectura y escritura ("a")
archivo = open("archivo2.txt", "a")
archivo.write("Hola mundo")
archivo.close()

#abrir en modo lectura y escritura ("a+")
archivo = open("archivo2.txt", "a+")
archivo.write("Hola mundo")
archivo.close()

#abrir en modo lectura y escritura ("x")
archivo = open("archivo2.txt", "x")
archivo.write("Hola mundo")
archivo.close()
'''