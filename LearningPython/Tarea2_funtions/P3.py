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

def slope (x1,y1,x2,y2):
    #m = X2-Y2/X1-Y1
    return (y1-(y2))/(x1-(x2))


def interseccion(x1,y1,m):
    #b = Y1- m(x1)
    return   y1 -(m*x1)
                        
def show(m,b):
     print(f"\nla solucion es Y={m}X{b}\n")

def Solucion(x1,y1,x2,y2):
    m=slope (x1,y1,x2,y2)
    print(m)
    b=interseccion(x1 ,y1,m)
   
    show(int(m),int(b))


def Var_cof():
    try:
        return [float(input(f'Ingrese el valor {coef}: ')) for coef in ('x1', 'y1', 'x2','y2')]
    except :
        print("\n!!!!Ingrese valores validos¡¡¡¡\n")
        Var_cof()

def Interfaz():
    print("Ecuacion Cuadratica\nIngrese valores\n")
    x1,y1,x2,y2=Var_cof()
    Solucion(x1,y1,x2,y2)
    Retorno()
    
 
def Bienvenida():
    print("----Bienvenido---- Vamos a resolver una ecuacion lineal:")
    print("    y=mx+b\n")

Bienvenida()
Interfaz()
