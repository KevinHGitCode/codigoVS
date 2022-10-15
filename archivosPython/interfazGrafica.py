#crear una interfaz grafica que tenga un boton sin funcionalidad

#importar librerias
from tkinter import *

#crear una ventana
ventana = Tk()

#dimensiones de la ventana: 300x300
ventana.geometry("300x300")
#titulo de la ventana
ventana.title("Interfaz grafica")
#no modificar el tamaño de la ventana
ventana.resizable(0,0)
#posicion inicial de la ventana: null
ventana.geometry("+0+0")


#crear un label
label = Label(ventana, text="Hola mundo")
label.pack()
#pocicionar el label en la ventana 50x150
label.place(x=50, y=150)

#crear un boton
boton = Button(ventana, text="Boton")
boton.pack()
#pocicionar el boton en la ventana 250x150
boton.place(x=250, y=150)

#TODO: crear una interfaz grafica que tenga un boton sin funcionalidad