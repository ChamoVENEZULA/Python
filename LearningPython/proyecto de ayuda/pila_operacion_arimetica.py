from ast import IsNot, Lambda
import string


class Pila():
    def __init__(self):
     self._lista =[]

    def push (self, valor):
     self._lista.append(valor)

    def pop (self): 
     return self._lista.pop()
    
    def pila_vacia (self):
     return self._lista
    
    def largo (self):
      return self.size()
    
    def tamaño (self):
      return len(self._lista)

    def ver_pila (self):
        print(self._lista) 
    
    def evaluar_expresion_postfija(self, postfija):

        pila = Pila()
        if postfija.isalnum()==False:
            
            postfija=str(sorted(postfija,reverse= True) )
            print(postfija)

numeros= []
operaciones= []

menúprincipal= int (input("Menú principal: \n 1)Evaluar Expresión: \n 2)Salir: \n"))
while menúprincipal != 2:
  if menúprincipal == 1:


    expresion = input("Ingrese la expresión en notación aritmética POSTFIJA : ")
    resultado = Pila().evaluar_expresion_postfija(expresion)
    print ("El resultado es:", resultado)



  elif menúprincipal == 2:
    break
  else:
    print("ERROR, Por favor digite una de las dos opciones del menú")
  
  menúprincipal= int (input("Menú principal: \n 1)Evaluar Expresión: \n 2)Salir: \n"))



