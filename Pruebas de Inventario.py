import tkinter
from tkinter import *
from tkinter import scrolledtext
import re

colores = []
materiales = []
titulo = "Inventario de filamentos"


filamentos = {
    "0101VIP" : ["Print A Lot", "PLA", "Violeta", "Pastel",1,200],
    "0101AZC" : ["Print A Lot", "PLA", "Azul", "Comun", 1, 100],
    "0101ROC" : ["Print A Lot", "PLA", "Rojo", "Comun",1,25],
    "0201VEC" : ["Grillon3","PLA", "Verde","Comun",0,0],
}



#Variables necesarias
filamentos_en_stock = [
    key for key, value__ in filamentos.items() if value__[4] >= 1
]



for plas, value_ in filamentos.items():
    if (filamentos[plas][2]) not in colores:
        colores.append(value_[2])

for mat, value in filamentos.items():
    if value[1] not in materiales:
        materiales.append(filamentos[mat][1])



class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master


inicio = Tk()
inicio.wm_title("Inventario de filamentos")
inicio.geometry('310x250')

bienvenida = Label(inicio, text="Bienvenido al inventario de filamentos",font = ("Agency FB", 20))
bienvenida.grid(column=0,row=1)


confirmacion_eleccion = Label(inicio,text="Elegir una de las siguientes opciones:")
confirmacion_eleccion.grid(column=0,row=2)

def click():
    confirmacion_eleccion.config(text="Seleccionado!")

def go_back():
    ventana_filamentos_en_Stock.destroy()

def primer_opcion():
    global ventana_filamentos_en_Stock
    ventana_filamentos_en_Stock = tkinter.Toplevel()
    ventana_filamentos_en_Stock.geometry("300x150")
    ventana_filamentos_en_Stock.wm_title("Filamentos en Stock")
    contenido = scrolledtext.ScrolledText(ventana_filamentos_en_Stock, width=25,height=5,font = ("Century Gothic", 15))
    contenido.grid(column=0,row=0)
    contenido.insert(INSERT, "\n".join(filamentos_en_stock))
    volver = Button(ventana_filamentos_en_Stock,text="Volver",command=go_back)
    volver.grid(column=0,row=9)

opcion1 = Button(inicio,text="Filamentos en Stock(Por codigo)",command=primer_opcion)
opcion1.grid(column=0,row=3)
opcion2 = Button(inicio,text="Colores en Stock",command=click)
opcion2.grid(column=0,row=4)
opcion3 = Button(inicio,text="Materiales en Stock",command=click)
opcion3.grid(column=0,row=5)
opcion4 = Button(inicio,text="Agregar un filamento",command=click)
opcion4.grid(column=0,row=6)
opcion5 = Button(inicio,text="Actualizar datos de un filamento",command=click)
opcion5.grid(column=0,row=7)
opcion6 = Button(inicio,text="Salir",command=exit)
opcion6.grid(column=0,row=9)

inicio.mainloop()