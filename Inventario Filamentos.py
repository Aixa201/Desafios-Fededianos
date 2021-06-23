import os
import time

#Variables necesarias
filamentos_en_stock = []
colores = []
materiales = []
titulo = "Inventario de filamentos"


filamentos = {
    "0101VIP" : ["Print A Lot", "PLA", "Violeta", "Pastel",1,200],
    "0101AZC" : ["Print A Lot", "PLA", "Azul", "Comun", 1, 100],
    "0101ROC" : ["Print A Lot", "PLA", "Rojo", "Comun",1,25],
    "0201VEC" : ["Grillon3","PLA", "Verde","Comun",0,0],
}



for key in filamentos:
    if (filamentos[key][4]) >= 1:
        filamentos_en_stock.append(key)

for plas in filamentos:
    if (filamentos[plas][2]) not in colores:
        colores.append(filamentos[plas][2])

for mat in filamentos:
    if (filamentos[mat][1]) not in materiales:
        materiales.append(filamentos[mat][1])



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
        os.system(command)

def bienvenida():
    print (titulo.center(50, "*"))
    print("Elegi el numero que corresponda a tu consulta")
    print("1 - Filamentos en Stock(Por codigo)")
    print("2 - Colores en Stock")
    print("3 - Materiales en Stock")
    print("4 - Agregar un filamento")
    print("5 - Actualizar datos de un filamento")
    print("6 - Ninguna de las anteriores")

def opcion_no_valida(respuesta):
    if respuesta not in range (1,6):
        print(f"No existe la opcion {respuesta}, intentelo nuevamente")
        clearConsole()


def primer_opcion(respuesta):
    if respuesta == 1: 
        print(filamentos_en_stock)
        time.sleep(2)
        print("Gracias por utilizar el Inventario de Filamentos")
        time.sleep(3)
        clearConsole()

def segunda_opcion(respuesta):
    if respuesta == 2:
        print(colores)
        time.sleep(2)
        print("Gracias por utilizar el Inventario de Filamentos")
        time.sleep(3)
        clearConsole()

def tercera_opcion(respuesta):
    if respuesta == 3:
        print(materiales)
        time.sleep(2)
        print("Gracias por utilizar el Inventario de Filamentos")
        time.sleep(3)
        clearConsole()


def opcion_4_marca(marca):
    if marca == 1 or marca == 2:
        time.sleep(0.5)
        print("Marca Agregada!")
        time.sleep(0.5)
    elif marca not in range(1,2):
        print("Volver a ingresar")
        time.sleep(1)
        clearConsole()
    return marca

def opcion_4_material(material):
    if material == 1 or material == 2 or material == 3:
        time.sleep(0.5)
        print("Tipo de Material Agregado!")
    elif material not in range(1,3):
        print("Volver a ingresar")
        time.sleep(1)
        clearConsole()
    return material

def opcion_4_color(color):
    if type(color) == str:
        print(f"Agregaste el siguiente color: {color}")
        time.sleep(0.5)
    return color


def opcion_4_tipo_color(tipo_color):
    global tipo_color_n
    if tipo_color not in range(1,6):
        print("Volver a ingresar")
        time.sleep(1)
        clearConsole()
    elif tipo_color == 1:
        print("Tipo de color agregado")
        tipo_color_n = "Comun"
    elif tipo_color == 2:
        print("Tipo de color agregado")
        tipo_color_n = "Pastel"
    elif tipo_color == 3:
        print("Tipo de color agregado")
        tipo_color_n = "Metalizado"
    elif tipo_color == 4:
        print("Tipo de color agregado")
        tipo_color_n = "Especial"
    elif tipo_color == 5:
        print("Tipo de color agregado")
        tipo_color_n ="Translucido"
    elif tipo_color == 6:
        print("Tipo de color agregado")
        tipo_color_n = "UV"
    return tipo_color_n


def generador_codigo_dicc(marca, material, color, tipo_color_n):
    global marca_n
    global material_n
    global nombre_nuevo_filamento
    global tipo_color_dicc
    if marca == 1:
        marca_n = "01"
    elif marca == 2:
        marca_n = "02"
    elif marca == 3:
        marca_n = "03"
    if material == 1:
        material_n = "01"
    elif material == 2:
        material_n = "02"
    elif material == 3:
        material_n = "03"
    if tipo_color_n == "Comun":
        tipo_color_dicc = tipo_color_n[0]
    elif tipo_color_n == "Pastel":
        tipo_color_dicc = tipo_color_n[0]
    elif tipo_color_n == "Metalizado":
        tipo_color_dicc = tipo_color_n[0]
    elif tipo_color_n == "Especial":
        tipo_color_dicc = tipo_color_n[0]
    elif tipo_color_n == "Translucido":
        tipo_color_dicc = tipo_color_n[0]
    elif tipo_color_n == "UV":
        tipo_color_dicc = tipo_color_n[0]
    nombre_nuevo_filamento = f"{marca_n}{material_n}{color[0:2]}{tipo_color_dicc}"
    return nombre_nuevo_filamento

def msj_codigo_creado(nombre_nuevo_filamento):
    if nombre_nuevo_filamento not in filamentos:
        print(f"El codigo asignado para el nuevo filamento es {nombre_nuevo_filamento}")
        print("Añadiendo filamento...")
    else:
        print("Ya esta registrado")

def descripcion_nuevo_filamento(marca_n,material_n,nombre_nuevo_filamento,color,tipo_color_n,cantidad,peso):
    global marca_dicc
    global material_dicc
    if marca_n == "01":
        marca_dicc = "Print A Lot"
    elif marca_n == "02":
        marca_dicc = "Grillon3"
    if material_n == "01":
        material_dicc = "PLA"
    elif material_n == "02":
        material_dicc = "PETG"
    elif material_n == "03":
        material_dicc = "FLEX"
    filamentos[nombre_nuevo_filamento] = [marca_dicc,material_dicc,color,tipo_color_n,cantidad,peso]
    time.sleep(1)

def filamento_añadido(nombre_nuevo_filamento):
    print(f"Codigo: {nombre_nuevo_filamento} Descripcion: {filamentos[nombre_nuevo_filamento]}")
    time.sleep(3)
    print("Actualmente estos son los filamentos registrados:")
    for i in filamentos:
        print(f" {i} , {filamentos[i]}")
        time.sleep(3)
    print("Gracias por utilizar el Inventario de Filamentos")
    time.sleep(2)
    clearConsole()

def cuarta_opcion(respuesta):
    global marca
    global material
    global color
    global tipo_color
    global cantidad
    global peso
    if respuesta == 4:
        print("¿De que marca es el nuevo filamento?")
        print("1 - Print A Lot")
        print("2 - Grillon3")
        marca = int(input())
        opcion_4_marca(marca)
        print("¿De que material es el nuevo filamento?")
        print("1 - PLA")
        print("2 - PETG")
        print("3 - FLEX")
        material = int(input())
        opcion_4_material(material)
        print("¿De que color es el nuevo filamento?")
        print("Ingresar en Mayusculas")
        color = input()
        time.sleep(0.5)
        opcion_4_color(color)
        print("¿Que tipo de color es?")
        print("1 - Comun")
        print("2 - Pastel")
        print("3 - Metalizado")
        print("4 - Especial")
        print("5 - Translucido")
        print("6 - UV")
        tipo_color = int(input())
        opcion_4_tipo_color(tipo_color)
        print("¿Cuantas bobinas hay del filamento?")
        cantidad = int(input())
        time.sleep(0.5)
        print("¿Cual es el peso del filamento sin contar el peso de la bobina?")
        peso = int(input())
        time.sleep(0.5)
        generador_codigo_dicc(marca, material, color, tipo_color_n)
        msj_codigo_creado(nombre_nuevo_filamento)
        descripcion_nuevo_filamento(marca_n,material_n,nombre_nuevo_filamento,color,tipo_color_n,cantidad,peso)
        filamento_añadido(nombre_nuevo_filamento)

def opcion_5_mod_marca(respuesta_opc_5):
    global mod_marca
    global marca_act
    if respuesta_opc_5 == 1:
        print("Usted desea cambiar el siguiente valor:")
        print((filamentos[filamento_a_mod][0]))
        time.sleep(2)
        print("¿A que valor desea modificarlo?")
        print("1 - Print A Lot")
        print("2 - Grillon3")
        mod_marca = int(input())
        time.sleep(2)
        if mod_marca == 1:
            marca_act = "Print A Lot"
            if filamentos[filamento_a_mod][0] == marca_act:
                print("El filamento es de la marca seleccionada")
            elif filamentos[filamento_a_mod][0] != marca_act:
                filamentos[filamento_a_mod][0] = marca_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod]) 
        elif mod_marca == 2:
            marca_act = "Grillon3"
            if filamentos[filamento_a_mod][0] == marca_act:
                print("El filamento es de la marca seleccionada")
            elif filamentos[filamento_a_mod][0] != marca_act:
                filamentos[filamento_a_mod][0] = marca_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod]) 
        else: 
            print("Volver a ingresar")
            time.sleep(2)
            clearConsole




def opcion_5_mod_material(respuesta_opc_5):
    global mod_material
    global material_act
    global nombre_mod_filamento
    if respuesta_opc_5 == 2:
        print("Usted desea cambiar el siguiente valor:")
        print((filamentos[filamento_a_mod][1]))
        time.sleep(1)
        print("¿A que valor desea modificarlo?")
        print("1 - PLA")
        print("2 - PETG")
        print("3 - FLEX")
        mod_material = int(input)
        time.sleep(2)
        if mod_material == 1:
            material_act = "PLA"
            if filamentos[filamento_a_mod][1] == material_act:
                print("El filamento es del material seleccionado")
            elif filamentos[filamento_a_mod][1] != material_act:
                filamentos[filamento_a_mod][1] = material_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
        elif mod_material == 2:
            material_act = "PETG"
            if filamentos[filamento_a_mod][1] == material_act:
                print("El filamento es del material seleccionado")
            elif filamentos[filamento_a_mod][1] != material_act:
                filamentos[filamento_a_mod][1] = material_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
        elif mod_material == 3:
            material_act = "FLEX"
            if filamentos[filamento_a_mod][1] == material_act:
                print("El filamento es del material seleccionado")
            elif filamentos[filamento_a_mod][1] != material_act:
                filamentos[filamento_a_mod][1] = material_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
        else: 
            print("Volver a ingresar")
            time.sleep(2)
            clearConsole

def opcion_5_mod_color(respuesta_opc_5):
    global mod_color
    global si_no
    if respuesta_opc_5 == 3:
        print("Usted desea cambiar el siguiente valor:")
        print((filamentos[filamento_a_mod][2]))
        time.sleep(2)
        print("¿A que color desea modificarlo?")
        print("Ingresar en mayusculas")
        print("Ejemplo: DORADO")
        mod_color = input()
        time.sleep(2)
        print(f"¿Confirma la modificacion al color {mod_color}?")
        print("1 - Si")
        print("2 - No")
        si_no = int(input())
        time.sleep(2)
        if si_no == 1:
            if filamentos[filamento_a_mod][2] != mod_color:
                filamentos[filamento_a_mod][2] = mod_color
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][2] == mod_color:
                print("El filamento es del color mencionado")
        elif si_no == 2:
            print("Cancelando modificacion...")
            print("Gracias por utilizar el inventario de filamentos")
            clearConsole()


def opcion_5_mod_tipo_color(respuesta_opc_5):
    global mod_tipo_color
    global tipo_color_act
    if respuesta_opc_5 == 4:
        print("Usted desea cambiar el siguiente valor:")
        print((filamentos[filamento_a_mod][3]))
        time.sleep(2)
        print("¿A que tipo de color quiere modificarlo?")
        print("1 - Comun")
        print("2 - Pastel")
        print("3 - Metalizado")
        print("4 - Especial")
        print("5 - Translucido")
        print("6 - UV")
        mod_tipo_color = int(input)
        time.sleep(2)
        if mod_tipo_color == 1:
            tipo_color_act = "Comun"
            if filamentos[filamento_a_mod][3] != tipo_color_act:
                filamentos[filamento_a_mod][3] = tipo_color_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][3] == tipo_color_act:
                print("El filamento es del tipo de color seleccionado")
        elif mod_tipo_color == 2:
            tipo_color_act = "Pastel"
            if filamentos[filamento_a_mod][3] != tipo_color_act:
                filamentos[filamento_a_mod][3] = tipo_color_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][3] == tipo_color_act:
                print("El filamento es del tipo de color seleccionado")
        elif mod_tipo_color == 3:
            tipo_color_act = "Metalizado"
            if filamentos[filamento_a_mod][3] != tipo_color_act:
                filamentos[filamento_a_mod][3] = tipo_color_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][3] == tipo_color_act:
                print("El filamento es del tipo de color seleccionado")
        elif mod_tipo_color == 4:
            tipo_color_act = "Especial"
            if filamentos[filamento_a_mod][3] != tipo_color_act:
                filamentos[filamento_a_mod][3] = tipo_color_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][3] == tipo_color_act:
                print("El filamento es del tipo de color seleccionado")
        elif mod_tipo_color == 5:
            tipo_color_act = "Translucido"
            if filamentos[filamento_a_mod][3] != tipo_color_act:
                filamentos[filamento_a_mod][3] = tipo_color_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][3] == tipo_color_act:
                print("El filamento es del tipo de color seleccionado")
        elif mod_tipo_color == 6:
            tipo_color_act = "UV"
            if filamentos[filamento_a_mod][3] != tipo_color_act:
                filamentos[filamento_a_mod][3] = tipo_color_act
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][3] == tipo_color_act:
                print("El filamento es del tipo de color seleccionado")



def opcion_5_mod_cantidad(respuesta_opc_5):
    global mod_cantidad
    global si_no
    if respuesta_opc_5 == 5:
        print("Usted desea cambiar el siguiente valor:")
        print((filamentos[filamento_a_mod][4]))
        time.sleep(2)
        print("¿A que valor desea modificarlo?")
        mod_cantidad = input()
        time.sleep(1)
        print(f"¿Confirma la modificacion al valor {mod_cantidad}?")
        print("1 - Si")
        print("2 - No")
        si_no = int(input())
        time.sleep(2)
        if si_no == 1:
            if filamentos[filamento_a_mod][4] != mod_cantidad:
                filamentos[filamento_a_mod][4] = mod_cantidad
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][4] == mod_cantidad:
                print("El filamento ya contiene la informacion")
        elif si_no == 2:
            print("Cancelando modificacion...")
            print("Gracias por utilizar el inventario de filamentos")
            time.sleep(2)
            clearConsole()


def opcion_5_mod_peso(respuesta_opc_5):
    global mod_peso
    global si_no
    if respuesta_opc_5 == 6:
        print("Usted desea cambiar el siguiente valor:")
        print((filamentos[filamento_a_mod][5]))
        time.sleep(2)
        print("¿A que valor desea modificarlo?")
        mod_peso = input()
        time.sleep(2)
        print(f"¿Confirma la modificacion al color {mod_peso}?")
        print("1 - Si")
        print("2 - No")
        si_no = int(input())
        time.sleep(2)
        if si_no == 1:
            if filamentos[filamento_a_mod][5] != mod_peso:
                filamentos[filamento_a_mod][5] = mod_peso
                print ("Descripcion actualizada:")
                print(filamentos[filamento_a_mod])
            elif filamentos[filamento_a_mod][5] == mod_peso:
                print("El filamento ya contiene la informacion")
        elif si_no == 2:
            print("Cancelando modificacion...")
            print("Gracias por utilizar el inventario de filamentos")
            clearConsole()


def quinta_opcion(respuesta):
    global filamento
    global respuesta_opc_5
    global filamento_a_mod
    if respuesta == 5:
        print("¿Que filamento desea modificar?")
        print("Escriba la opcion tal y como aparece")
        print("Ejemplo: 0101VIP")
        for filamento in filamentos:
            print(f"{filamento}")
            time.sleep(1)
        filamento_a_mod = input()
        time.sleep(2)
        if filamento_a_mod in filamentos:
            print("Los detalles del filamento seleccionado son:")
            print (filamentos[filamento_a_mod])
            print("¿Que desea modificar?")
            print("1 - Marca")
            print("2 - Material")
            print("3 - Color")
            print("4 - Tipo de Color")
            print("5 - Cantidad de Bobinas")
            print("6 - Peso total")
            respuesta_opc_5 = int(input())
            opcion_5_mod_marca(respuesta_opc_5)
            opcion_5_mod_material(respuesta_opc_5)
            opcion_5_mod_color(respuesta_opc_5)
            opcion_5_mod_tipo_color(respuesta_opc_5)
            opcion_5_mod_cantidad(respuesta_opc_5)
            opcion_5_mod_peso(respuesta_opc_5)
        else: 
            print("Volver a ingresar")
            clearConsole()




def programa():
    while True:
        bienvenida()
        respuesta = int(input())
        primer_opcion(respuesta)
        segunda_opcion(respuesta)
        tercera_opcion(respuesta)
        cuarta_opcion(respuesta)
        quinta_opcion(respuesta)


#En opcion 5 cambiar tambien codigo del filamento
#En opcion 4 preguntar si se quiere ver la lista de todos los filamentos
#Agregar mas pausas
#Buscar como registrarlo en un archivo aunque sea txt

programa()