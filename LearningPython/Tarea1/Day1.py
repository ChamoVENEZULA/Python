"""Escribir programa que lea 2 varible y diga si es menor, mayor o igual"""


num=int(input("Primera Variable\n"))
num2=int(input("Segunda Variable\n"))

if num==num2:
    print("Son iguales")
elif num>num2:
    print(str(num) + " Es mayor")
else:
    print(str(num2)+" Es mayor")
    
""" Escriba un programa que lea un numero, y luego le pida al usuario tantos numeros como el primer
numero introducido (o sea, primero se pide un numero, el usuario introduce digamos 2. Entonces
a continuacion el programa pide 2 numeros; si el usuario hubiera escrito 6, pues pide 6 el
usuario escribio 100 Pues pide 100 """

num=int(input("Primera Variable\n"))

arreglo=[]

for x in range(num):
    arreglo.append(int(input('ingrese variable: '+ str(int(x+1)) + "\n")))
 
for x in arreglo:
    print(str(x),end=", ")

""" Haga un nuevo programa, basado en el anterior. Y ahora mete todos los numeros en una lista
(excepto el primero) y luego imprime la lista"""

num=int(input("Primera Variable\n"))

arreglo=[]

for x in range(num):
    if x==0:
        int(input('ingrese variable: '+ str(int(x+1)) + "\n"))
    else:
        arreglo.append(int(input('ingrese variable: '+ str(int(x+1)) + "\n")))
 
for x in arreglo:
    print(str(x),end=", ")