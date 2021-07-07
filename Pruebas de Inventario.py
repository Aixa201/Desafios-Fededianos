from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master


inicio = Tk()
inicio.wm_title("Inventario de filamentos")
inicio.geometry('400x200')

bienvenida = Label(inicio, text="Bienvenido al inventario de filamentos",font = ("Agency FB", 20))
bienvenida.grid(column=0,row=1)


confirmacion_eleccion = Label(inicio,text="Elegir una de las siguientes opciones:")
confirmacion_eleccion.grid(column=0,row=2)

def click():
    confirmacion_eleccion.config(text="Primera opcion!")

opcion1 = Button(inicio,text="Filamentos en Stock(Por codigo)",command=click)
opcion1.grid(column=0,row=3)

inicio.mainloop()