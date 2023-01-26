""" Escriba un programa que muestra un menu de 4 opciones al usuario:
1- Leer lista de numeros
2- Imprimir numero mas grande
3- Imprimir numero mas pequeno
4- Salir.
Luego de imprimir dicho menu, el programa espera que el usuario escriba una opcion, 
especificamente un numero entre 1 y 4. Si el usuario digita algo diferente, 
el programa imprime ERROR, OPCION NO RECONOCIDA
Si oprime 4, el programa termina."""

print("1- Leer lista de numeros \n2- Imprimir numero mas grande \n3- Imprimir numero mas pequeno \n4- Salir.")


def respuesta():
    try:
        lang = int(input("Selecione una opcion: "))
        return lang
    except :
        print("OPCION NO RECONOCIDA \nIntente nuevamente")
        respuesta()
     
def menu():
    match respuesta():
        case 1:
            print("Good job")
            menu()
        case 2:
            print("You are a good Data Scientist")
            menu()
        case 3:
            print("You are a excelent developer")
            menu()
        case 4:
            print("Programa finalizado")
            return
        case _:
            print("no existe opcion, solo hay 4")
            menu()

menu()