import os
from pathlib import Path, PurePath

#funcion obtener el directorio actual con os (<class 'str'>)
def getRuta():
    return os.getcwd()

#funcion obtener el directorio actual con pathlib (<class 'pathlib.Path'>)
def getRutaPathlib():
    return Path.cwd()

#funcion listar los archivos de un directorio con os (<class 'list'>)
def getDir():
    return os.listdir()

#funcion listar los archivos de un directorio con pathlib (<class 'generator'>)
def getDirPathlib():
    return list(Path().iterdir())

#funcion listar los archivos de un directorio como parametro con os (<class 'list'>)
def getListDir(directorio):
    return os.listdir(directorio)

#funcion juntar dos rutas con os (<class 'str'>)
def joinRuta(ruta1, ruta2):
    #call funciones
    #print(getRuta())
    #print(joinRuta(getRuta(), 'VScode'))
    return os.path.join(ruta1, ruta2)

#funcion juntar dos rutas con pathlib (<class 'pathlib.PureWindowsPath'>)
def joinRutaPathlib(ruta1, ruta2):
    return PurePath(ruta1).joinpath(ruta2)

#funcion crear carpeta
def crearCarpeta(nameCarpeta):
    os.mkdir(nameCarpeta)
    return 'Carpeta creada'

#funcion crear carpeta con pathlib
def crearCarpetaPathlib(nameCarpeta):
    Path(nameCarpeta).mkdir(parents=True, exist_ok=True)
    return 'Carpeta creada'

#crear una carpeta con otra dentro 
def crearCarpetaDentro(carpetaDentro, carpetaDestino):
    os.makedirs(os.path.join(carpetaDestino, carpetaDentro))
    # O tambien: os.makedirs(carpetaDestino + '/' + carpetaDentro)
    return 'Carpeta creada'

#crear una carpeta con otra dentro con pathlib
def crearCarpetaDentroPathlib(carpetaDentro, carpetaDestino):
    Path(carpetaDestino).joinpath(carpetaDentro).mkdir(parents=True, exist_ok=True)
    return 'Carpeta creada'

#funcion renombrar carpeta
def renombrarCarpeta(carpeta, nuevoNombre):
    os.rename(carpeta, nuevoNombre)
    return 'Carpeta renombrada'

#funcion renombrar carpeta con pathlib
def renombrarCarpetaPathlib(carpeta, nuevoNombre):
    Path(carpeta).rename(nuevoNombre)
    # O tambien: Path.rename(carpeta, nuevoNombre)
    return 'Carpeta renombrada'

#funcion renombrar varios archivos
def renombrarVariosArchivos(listaArchivos):
    for fiel in getDir():
        if fiel.endswith('.txt'):

            os.rename(fiel, fiel.replace('.txt', '.py'))
            
            # O tambien: os.rename(fiel, f'2021_{fiel}')

# funcion existe ruta o carpeta
def existeRuta(ruta):
    return os.path.exists(ruta)
    #print(existeRuta('archivosPython' in 'VScode'))

#print(os.path.abspath('VScode/archivosPython/osAndPath.py'))

#funcion eliminar carpeta
def eliminarCarpeta(carpeta):
    os.rmdir(carpeta)
    return 'Carpeta eliminada'

#funcion eliminar archivo
def eliminarArchivo(archivo):
    os.remove(archivo)
    return 'Archivo eliminado'

#funcion buscar archivo
def buscarArchivo(archivo):
    return os.path.isfile(archivo)
    #print(buscarArchivo('VScode/archivosPython/osAndPath.py'))

#renombrarCarpeta('VScode/archivosPython/osAndPath.py', 'VScode/archivosPython/os_&&_path.py')

#eliminar los archivos .class de C:\Users\C.univercitaria-k\Desktop\test-atom\Learn
def eliminarArchivosClass():
    listRuta=os.listdir(os.path.join(os.getcwd(), 'Curso_Ingles'))
    ruta=os.path.join(os.getcwd(), 'Curso_Ingles')
    for fiel in listRuta:
        listRuta2=os.listdir(os.path.join(ruta, fiel))
        ruta2=os.path.join(ruta, fiel)
        for fiel2 in listRuta2:
            if fiel2.endswith('.html'):
                print(f'Eliminando archivo: {fiel2}: {ruta2}/{fiel2}')
                os.remove(os.path.join(ruta2, fiel2))
    return 'Archivos eliminados'

#print(os.listdir(os.path.join(os.getcwd(), 'Curso_Ingles')))
#eliminarArchivosClass()

#print('Bucles.class' in os.listdir(os.path.join(os.getcwd(), 'Learn')))
#eliminarArchivosClass()

#funcion carpeta esta vacia
#TODO: funcion carpeta esta vacia

