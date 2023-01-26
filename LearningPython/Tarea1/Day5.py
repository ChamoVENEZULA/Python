"""- Usando el programa del dia anterior, implemente las opciones 1, 2 y 3 de la siguiente forma
o Si presiona 1, el programa leera una lista de numeros separados por coma, la cargara como una lista de enteros que imprimira.
o Si presiona 2, el programa recorrera la lista de numeros cargada en el paso 1, e imprimira el numero mas grande
o Si presiona 3, el programa recorrera la lista de numeros cargada en el paso 1, e imprimira el numero mas pequeno
Hagalo usado funciones
- Al menos intentelo. Si no puede, hagalo de corrido."""

from typing import List


print("1- Leer lista de numeros \n2- Imprimir numero mas grande \n3- Imprimir numero mas pequeno \n4- Salir.")

def lista():
     Nlista = "8,9,7,52,46,5,4"
     arreglo = Nlista.split(",")
     arreglo =[int(x) for x in arreglo]
     return arreglo

def respuesta():
    try:
        lang = int(input("Selecione una opcion: "))
        return lang
    except :
        print("OPCION NO RECONOCIDA \nIntente nuevamente")
        respuesta()

def Mayor(lista):
    mayor=0
    for x in range(len(lista)):
        if(x==0):
            mayor=lista[x]
        elif(mayor>lista[x]):
            continue
        else:
            mayor=lista[x]

    return mayor

def Menor(lista):
    menor=0
    for x in range(len(lista)):
        if(x==0):
            menor=lista[x]
        elif(menor<lista[x]):
            continue
        else:
            menor=lista[x]

    return menor

def menu():
    match respuesta():
        case 1:
            
            print(lista())
            print()
            menu()

        case 2:

            print(Mayor(lista()))
            menu()

        case 3:
            print(Menor(lista()))
            menu()

        case 4:
            print("Programa finalizado")
            return
        case _:
            print("no existe opcion, solo hay 4")
            menu()


menu()
