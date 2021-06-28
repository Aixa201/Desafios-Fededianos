import cmath

a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))

raiz_cuadrada = (pow(b,2))-(4*a*c)
raiz_cuadrada == pow(raiz_cuadrada,0.5)
x1 = 0
x2 = 0



def calculadora(a,b,c):
    xv = -(b)/2*a
    yv = a * pow(xv, 2) + (b * xv) + c
    vertice = (xv,yv)
    ejedesimetria = -b / (2*a)
    print(f"Las coordenadas del vertice son {vertice}")
    print(f"El eje de simetria es: {ejedesimetria}")
    print(f"La ordenada al origen es: {c}")
    if raiz_cuadrada >= 0:
        x1 == (-b + raiz_cuadrada)/2*a
        x2 == (-b - raiz_cuadrada)/2*a
        if x1 == 0 and x2 == 0:
            print("La funcion no tiene raices")
        elif x1 != x2:
            print(f"Las raices son: {x1} y {x2}")
        elif x1 == x2:
            print(f"Tiene una unica raiz: {x1}")
    elif raiz_cuadrada < 0:
        print("La funcion no tiene raices")
    if a > 0:
        print("La funcion abre para arriba")
    elif a < 0:
        print("La funcion abre para abajo")

if a == 0:
    print("A es invalida")
else:
    calculadora(a,b,c)
