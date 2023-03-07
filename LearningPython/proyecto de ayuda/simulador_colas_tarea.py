import numpy as np 
from scipy.stats import poisson

class simulador_colas():
    def __init__(self):
        self.__lista = []

    def enqueue(self, valor):
        self.__lista.append(valor)

    def dequeue(self):
        return self.__lista.pop(0)
    
    def cola_vacia(self):
        return len(self.__lista) == 0
     
    def ver_cola(self):
        print(self.__lista)

class Persona:
    def __init__(self, id_):
        self.id = id_
        self.hora_llegada = np.round(poisson.rvs(mu=10, size=1), 2) 

    def __str__(self):
        return f"Persona {self.id} llegó a las {self.hora_llegada} segundos"

personas = []
for i in range(10):
    persona = Persona(i+1)
    personas.append(persona)
    print(persona)


def main():
        valores = simulador_colas()
        valores.enqueue(7)
        valores.enqueue(8)
        valores.enqueue(1)
        valores.enqueue(2)
        valores.enqueue(2)

        
main()