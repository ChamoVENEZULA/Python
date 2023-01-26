"""Escriba un programa que lea una lista de numeros introducida por el usuario 
(lea cada numero, uno por uno.. .como en el dia 1), luego la imprime y SIN USAR LA FUNCION REVERSE,
le de vuelta (es decir, invierta el orden de los numeros) y la vuelve a imprimir"""

num = int(input("coloque la cantidad de numero que desea ingresar: ") )
lista=[]
for x in range (num):
    lista.append(int(input("Ingrese variable " + str(x+1)+" : " ) ))

print("Lista normal ->",lista)

print("Lista invertida ->",lista[::-1])

"""Haga un programa que lea una lista de numeros introducidos por el usuario 
y luego extraiga a una nueva lista solo los numeros pares."""
num2 = int(input("coloque la cantidad de numero que desea ingresar: ") )
lista=[]
lista2=[]
for x in range (num2):
    lista.append(int(input("Ingrese variable " + str(x+1)+" : " ) ))

for x in lista:
    if x%2==0:
        lista2.append(x)

print(lista2)