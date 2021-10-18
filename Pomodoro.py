import datetime
#Variables de pomodoro
cantbloques = 4
bloque = 25 
descanso_corto = 5
descanso_largo = 15
respuesta = 0


#Mensaje inicial
def Inicio(): 
    while True:
        print(f"""
        Valores predeterminados de Pomodoro
        Cantidad de bloques: {cantbloques}
        Duracion de bloques: {bloque}
        Duracion de descansos cortos: {descanso_corto}
        Duracion de descansos largos: {descanso_largo}
        ¿Usar valores predeterminados? (S/N)""")
        break

#Pomodoro con valores predeterminados
def Predeterminado():
    print("¿Iniciar pomodoro? (S/N)")
    resp1 = input()
    if resp1 == "s" or resp1 == "S":
        print("Iniciando...")
    else:
        print("Pomodoro cancelado")


#Pomodoro personalizado
def Personalizado():
    cantbloques_personalizado = input("Cantidad de bloques: ")
    bloque = input("Duracion de bloques: ")
    descanso_corto = input("Duracion de descansos cortos: ")
    descanso_largo = input("Duracion de descansos largos: ")
    print("¿Confirmas estos valores? (S/N)")
    respuesta = input()

def Temporizador(z,x,y):
    x = bloque
    

Inicio()
respuesta = input()
if respuesta == "s" or respuesta == "S":
    Predeterminado()
    Temporizador()
elif respuesta == "n" or respuesta == "N":
    Personalizado()
    Temporizador()
else:
    print("Volver a ingresar")