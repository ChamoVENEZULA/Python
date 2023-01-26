"""
Haga un programa con funciones, donde
o Se pide al usuario que digite un numero y lo retorna
o Se usa el numero leido como parametro de OTRA FUNCION que calcula la sumatoria desde 1 hasta el numero leido
o Se imprime el resultado.
"""


def ingreso():
    try:
        return int(input("ingrese numero para la sumatoria: "))
    except :
        print("esto no es un numero entero, intenta de nuevo")
        ingreso()

def sumatoria(ingreso):
    total=1

    for x in range(ingreso+1):
        total+=x

    return total

def interfaz():

   print( sumatoria(ingreso()))

interfaz()