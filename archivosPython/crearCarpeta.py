'''#crear un programa que haga una carpeta y un archivo en ella
import os
os.mkdir("carpeta")
os.chdir("carpeta")
f = open("archivo.txt", "w")
f.write("Hola mundo")
f.close()
os.chdir("..")
os.rmdir("carpeta")
print("Carpeta y archivo creados")
#-----------------------------------------------------------------------------------
#!/usr/bin/env python3
# Path: archivosPython\crearCarpeta.py'''

#abrir un archivo y escribir

#TODO: crear un programa que haga una carpeta y un archivo en ella

#FIXME: es un comentario de error

#con bookmarks dejas una marca en el codigo con una etiqueta (usa la paleta de comandos para crear una (ctrl+shift+p))

#importar libreria os
import os
#importar libreria path

#funcion crear un archivo
def crearArchivo(nombreArchivo):
    #crear el archivo
    archivo = open(nombreArchivo, "w")
    #retornar el archivo
    return archivo
   


#funcion guardar archivo
def guardarArchivo(archivo, contenido):
    #escribir en el archivo
    archivo.write(contenido)
    #cerrar el archivo
    archivo.close()
    #retornar el archivo
    return archivo

#llamar a la funcion
crearArchivo("archivo.txt")
