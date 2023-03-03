#!/usr/local/bin/python
# coding: latin-1

from cmath import sqrt

def respuesta():
        return input("Desea repetir?\n-Si\n-No\n-->").lower()
    

def Retorno():
    match respuesta():
        case"si":
            Interfaz()
        case "no":
            print("!!!!!!!--Hasta Luego--¡¡¡¡¡¡¡¡¡¡")
        case _:
            print("opcion no reconocida, Intente nuevamente\n")
            Retorno()


def discandSolution(a,b,c):
    discriminante =  b * b - 4 * a * c

    if discriminante < 0:
       # comprobamos si no existen soluciones reales
       print(f'La ecuación no tiene soluciones reales.')

    else:
       raiz = sqrt(discriminante)      
       x_1 =(-b + raiz) / (2 * a)

       if discriminante != 0:          
        x_2 = (-b - raiz) / (2 * a),2
        print(f'Las soluciones son ->{ x_1 }<- y ->{ x_2 }<-.') 

       else:
        print(f'La única solución es x = {x_1}') 

def Var_cof():
    try:
        return [float(input(f'Ingrese el coeficiente {coef}: ')) for coef in ('A', 'B', 'C')]
    except :
        print("\n!!!!Ingrese valores validos¡¡¡¡\n")
        Var_cof()

def Interfaz():
    print("Ecuacion Cuadratica\nIngrese valores\n")
    a,b,c=Var_cof()
    discandSolution(a,b,c)
    Retorno()
    
 
def Bienvenida():
    print("----Bienvenido---- Vamos a resolver una ecuacion de segundo grado:")
    print("    ax² + bx + c = 0\n")

Bienvenida()
Interfaz()