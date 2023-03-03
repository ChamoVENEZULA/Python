#!/usr/local/bin/python
# coding: latin-1

import scipy.stats


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

                        
def show(m,b):
     print(f"\nla solucion es Y={m}X{b}\n")

def Solucion():
    par1,par2=Var_cof()
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(par1,par2)
    print(slope)
    print(intercept)
    



def Var_cof():
    var=[] 
    var2=[]
    try:
     
        var.append([float(input(f'Ingrese el valor {coef}: ')) for coef in ('x1', 'y1')])
        var2.append([float(input(f'Ingrese el valor {coef}: ')) for coef in ('x2', 'y1')])
        return  var,var2
    except :
        print("\n!!!!Ingrese valores validos¡¡¡¡\n")
        Var_cof()

def Interfaz():
    print("Ecuacion Cuadratica\nIngrese valores\n")
    Solucion()
    Retorno()
    
 
def Bienvenida():
    print("----Bienvenido---- Vamos a resolver una ecuacion lineal:")
    print("    y=mx+b\n")

Bienvenida()
Interfaz()
