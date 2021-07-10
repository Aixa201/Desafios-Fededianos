from os import lseek
import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

#Variables necesarias

colores = []
materiales = []
titulo = "Inventario de filamentos"


filamentos = {
    "0101VIP" :["Print A Lot", "PLA", "Violeta", "Pastel",1,200],
    "0101AZC" :["Print A Lot", "PLA", "Azul", "Comun", 1, 100],
    "0101ROC" :["Print A Lot", "PLA", "Rojo", "Comun",1,25],
    "0201VEC" :["Grillon3","PLA", "Verde","Comun",0,0],
}



#Variables necesarias
filamentos_en_stock = [
    key for key, value__ in filamentos.items() if value__[4] >= 1
]



for plas, value_ in filamentos.items():
    if (filamentos[plas][2]) not in colores and (filamentos[plas][4]) > 0:
        colores.append(value_[2])

for mat, value in filamentos.items():
    if value[1] not in materiales and (filamentos[mat][4]) > 0:
        materiales.append(filamentos[mat][1])


#Definicion de Window para tkinter

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

#Funcion para hacer que todas las opciones tengan a mano la guia

def help_window():
    ayuda = tkinter.Toplevel()
    ayuda.wm_title("Ayuda")
    contenido = scrolledtext.ScrolledText(ayuda, width=90, height=25)
    with open("Ayuda-Inv-Filamentos.txt") as fh:
        guia = fh.read()
    contenido.insert(END, guia)
    contenido.configure(state=DISABLED)
    contenido.grid(column=0, row=0)
    contenido.pack()
    menu_help = Menu(ayuda)
    menu_help.add_command(label='Volver', command=ayuda.destroy)
    ayuda.config(menu=menu_help)


#Definicion del menu

inicio = Tk()
inicio.wm_title("Inventario de filamentos")
inicio.geometry('350x300')
bienvenida = Label(inicio, text="Bienvenido al inventario de filamentos",font = ("Agency FB", 20))
bienvenida.grid(column=0, row=1, padx=10, pady=10)
menu = Menu(inicio)
new_item = Menu(menu, tearoff=0)
menu.add_command(label='Ayuda', command=help_window)
inicio.config(menu=menu)


#comando default para las que no estan definidas
def click():
    confirmacion_eleccion = Label(inicio,text="Elegir una de las siguientes opciones:")
    confirmacion_eleccion.grid(column=0, row=2, pady=1, padx=1 )
    confirmacion_eleccion.config(text="Seleccionado!")


#Ventana que se abre con la primera opcion
def primer_opcion():
    global ventana_filamentos_en_Stock 
    ventana_filamentos_en_Stock = tkinter.Toplevel()
    menu = Menu(ventana_filamentos_en_Stock)
    menu.add_command(label='Ayuda', command=help_window)
    ventana_filamentos_en_Stock.config(menu=menu)
    ventana_filamentos_en_Stock.geometry("300x150")
    ventana_filamentos_en_Stock.wm_title("Filamentos en Stock")
    contenido = scrolledtext.ScrolledText(ventana_filamentos_en_Stock, width=25,height=5,font = ("Century Gothic", 15))
    contenido.grid(column=0, row=0, padx=10, pady=10)
    contenido.insert(INSERT, "\n".join(filamentos_en_stock))
    volver = Button(ventana_filamentos_en_Stock,text="Volver",command=ventana_filamentos_en_Stock.destroy)
    volver.grid(column=0, row=9, pady=10, padx=10)

#Ventana que se abre con la segunda opcion
def segunda_opcion():
    global ventana_colores
    ventana_colores = tkinter.Toplevel()
    menu = Menu(ventana_colores)
    menu.add_command(label='Ayuda', command=help_window)
    ventana_colores.config(menu=menu)
    ventana_colores.geometry("300x150")
    ventana_colores.wm_title("Colores en Stock")
    contenido = scrolledtext.ScrolledText(ventana_colores, width=25,height=5,font = ("Century Gothic", 15))
    contenido.grid(column=0, row=0, pady=10, padx=10)
    contenido.insert(INSERT, "\n".join(colores))
    volver = Button(ventana_colores,text="Volver",command=ventana_colores.destroy)
    volver.grid(column=0, row=9, padx=10, pady=10)

def tercer_opcion():
    global ventana_materiales
    ventana_materiales = tkinter.Toplevel()
    menu = Menu(ventana_materiales)
    menu.add_command(label='Ayuda', command=help_window)
    ventana_materiales.config(menu=menu)
    ventana_materiales.geometry("300x150")
    ventana_materiales.wm_title("Materiales en Stock")
    contenido = scrolledtext.ScrolledText(ventana_materiales, width=25,height=5,font = ("Century Gothic", 15))
    contenido.grid(column=0, row=0, pady=10, padx=10)
    contenido.insert(INSERT, "\n".join(materiales))
    volver = Button(ventana_materiales,text="Volver",command=ventana_materiales.destroy)
    volver.grid(column=0, row=9, padx=10, pady=10)

def cuarta_opcion():
    global ventana_agregar
    ventana_agregar = tkinter.Toplevel()
    menu = Menu(ventana_agregar)
    menu.add_command(label="Ayuda", command=help_window)
    ventana_agregar.config(menu=menu)
    ventana_agregar.geometry("270x450")
    ventana_agregar.wm_title("Agregar filamento")
    titulo = Label(ventana_agregar, text="Seleccionar los siguientes datos")
    titulo.grid(column=0, row=0,padx=1)
    titulo_marca = Label(ventana_agregar, text="Marca:")
    titulo_marca.grid(column=0, row=1, padx=5)
    lista_marcas = Combobox(ventana_agregar)
    lista_marcas['values']= ("Seleccionar","PrintALot", "Grillon3", "MakerParts", "PlastAr", "GST")
    lista_marcas.current(0)
    lista_marcas.grid(column=0, row=2, padx=5)
    titulo_material = Label(ventana_agregar, text="Material:")
    titulo_material.grid(column=0, row=3, padx=5)
    lista_material = Combobox(ventana_agregar)
    lista_material['values']= ("Seleccionar","PLA", "PETG", "ABS", "FLEX")
    lista_material.current(0)
    lista_material.grid(column=0, row=4, padx=5)
    titulo_color = Label(ventana_agregar, text="Color:")
    titulo_color.grid(column=0, row=5, padx=5)
    entrada_color = Entry(ventana_agregar)
    entrada_color.grid(column=0, row=6, padx=5)
    titulo_tipo_color = Label(ventana_agregar, text="Tipo de Color:")
    titulo_tipo_color.grid(column=0, row=7, padx=5)
    lista_tipo_color = Combobox(ventana_agregar)
    lista_tipo_color['values']= ("Seleccionar","Comun", "Translucido", "Especial", "UV", "Glitter", "Bicolor", "Pastel", "Metalizado")
    lista_tipo_color.current(0)
    lista_tipo_color.grid(column=0, row=8, padx=5)
    titulo_bobinas = Label(ventana_agregar, text="Cantidad de bobinas:")
    titulo_bobinas.grid(column=0, row=9, padx=5)
    entrada_bobinas = Spinbox(ventana_agregar, from_=0, to=10, width=5)
    entrada_bobinas.grid(column=0, row=10, padx=5)
    titulo_peso = Label(ventana_agregar, text="Peso actual:")
    titulo_peso.grid(column=0, row=11, padx=5)
    entrada_peso = Entry(ventana_agregar)
    entrada_peso.grid(column=0, row=12, padx=5)
    titulo_pregunta_peso = Label(ventana_agregar, text="¿El peso ingresado incluye el peso de la bobina?")
    titulo_pregunta_peso.grid(column=0, row=13, padx=5)
    respuesta_pregunta_peso_si = Radiobutton(ventana_agregar, text="Si", value=1)
    respuesta_pregunta_peso_si.grid(column=0, row=14, padx=5)
    respuesta_pregunta_peso_no = Radiobutton(ventana_agregar, text="No", value=2)
    respuesta_pregunta_peso_no.grid(column=0, row=15, padx=5)
    boton_agregar = Button(ventana_agregar, text="Agregar")
    boton_agregar.grid(column=0, row=16, padx=5)




opcion1 = Button(inicio,text="Filamentos en Stock(Por codigo)",command=primer_opcion)
opcion1.grid(column=0,row=3, pady=5)
opcion2 = Button(inicio,text="Colores en Stock",command=segunda_opcion)
opcion2.grid(column=0,row=4, pady=5)
opcion3 = Button(inicio,text="Materiales en Stock",command=tercer_opcion)
opcion3.grid(column=0,row=5, pady=5)
opcion4 = Button(inicio,text="Agregar un filamento",command=cuarta_opcion)
opcion4.grid(column=0,row=6, pady=5)
opcion5 = Button(inicio,text="Actualizar datos de un filamento",command=click)
opcion5.grid(column=0,row=7, pady=5)
opcion6 = Button(inicio,text="Salir",command=exit)
opcion6.grid(column=0,row=9, pady=5)

inicio.mainloop()