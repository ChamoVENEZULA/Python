import re
class carro():
    color=''
    ruedas=4
    puertas=''
    def __init__(self, color, puertas):
        self.color= color
        self.puertas = puertas
        
    pass
class coche(carro):  
    velocimetro=''
    Cilindrada=''
    def __init__(self,color,puertas, velocimetro,cilindrada):
        super().__init__(color,puertas)
        self.velocimetro= velocimetro
        self.Cilindrada = cilindrada
                          
def insertar(x,y):
    if(y):
        j=input('ingrese '+x+': ')
        if bool(re.search(r'\d', j))==False:
            return j
        else:
            print('Error, intente de nuevo')
            insertar(x,y)
        
    else:
       try:
         return int(input('ingrese '+x+': '))  
       except :
           print('Ingrese Numero')
           insertar(x,y)

C=coche(insertar('color',True),insertar('puerta',False),insertar('Velocimetro',False),insertar('cilindrada',False))  

print(f'El carro es de color {C.color} tiene {C.puertas}\b'
      +f'su Velocimetro es de {C.velocimetro } \b'
      +f'y es de cilindrada {C.Cilindrada}')