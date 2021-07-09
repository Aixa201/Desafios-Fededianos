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
    if (filamentos[plas][2]) not in colores and (filamentos[plas][4]) > 0:
        colores.append(value_[2])

for mat, value in filamentos.items():
    if value[1] not in materiales and (filamentos[plas][4]) > 0:
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



def primer_opcion():
    global ventana_filamentos_en_Stock
    ventana_filamentos_en_Stock = tkinter.Toplevel()
    ventana_filamentos_en_Stock.geometry("300x150")
    ventana_filamentos_en_Stock.wm_title("Filamentos en Stock")
    contenido = scrolledtext.ScrolledText(ventana_filamentos_en_Stock, width=25,height=5,font = ("Century Gothic", 15))
    contenido.grid(column=0,row=0)
    contenido.insert(INSERT, "\n".join(filamentos_en_stock))
    volver = Button(ventana_filamentos_en_Stock,text="Volver",command=ventana_filamentos_en_Stock.destroy)
    volver.grid(column=0,row=9)

def segunda_opcion():
    global ventana_colores
    ventana_colores = tkinter.Toplevel()
    ventana_colores.geometry("300x150")
    ventana_colores.wm_title("Colores en Stock")
    contenido = scrolledtext.ScrolledText(ventana_colores, width=25,height=5,font = ("Century Gothic", 15))
    contenido.grid(column=0,row=0)
    contenido.insert(INSERT, "\n".join(colores))
    volver = Button(ventana_colores,text="Volver",command=ventana_colores.destroy)
    volver.grid(column=0,row=9)


def help_window():
    guia = open("Ayuda-Inv-Filamentos.txt", "wb")
    ayuda = tkinter.Toplevel()
    ayuda.wm_title("Ayuda")
    contenido = Text(ayuda)
    contenido.configure(state=DISABLED)
    contenido.insert(INSERT, guia.read)
    contenido.pack()

menu = Menu(inicio)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Ayuda', command=help_window)
menu.add_cascade(label='Opciones',menu=new_item)
inicio.config(menu=menu)


opcion1 = Button(inicio,text="Filamentos en Stock(Por codigo)",command=primer_opcion)
opcion1.grid(column=0,row=3)
opcion2 = Button(inicio,text="Colores en Stock",command=segunda_opcion)
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