"""Escriba un programa que lea una hilera de numeros, separados por “,”.
El programa separa los numeros y los convierte en una lista de ENTEROS y la imprime."""
import statistics

Nlista = "8,9,7,52,46,5,4"
arreglo = Nlista.split(",")

arreglo =[int(x) for x in arreglo]

print(arreglo)

"""  Escriba un programa que lea una hilera de números, separados por “,”.
El programa separa los números y los convierte en una lista de ENTEROS y 
la imprime. Luego el programa imprime el PROMEDIO de los números. Para calcular
elpromedio, escriba una función que reciba dicha lista."""

def prom(arreglo):
    promedio= statistics.mean(arreglo)
    return print( round(promedio,2))

Nlista = "8,9,7,2,6,5,4"
arreglo = Nlista.split(",")

arreglo =[int(x) for x in arreglo]

prom(arreglo)