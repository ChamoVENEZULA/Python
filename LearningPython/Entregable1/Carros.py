from telnetlib import SE


class auto:
    def __init__(self,modelo,color,year,precio,aceleracion):
        self.modelo = modelo
        self.color= color
        self.year = year
        self.precio= precio
        self.aceleracion=aceleracion
        self.desplazamiento=0
        

    def acelerar(self):
        
        self.desplazamiento+=self.aceleracion
        

    def retroceder(self):
        self.desplazamiento-=self.aceleracion

    def __str__(self):
        return f"{self.modelo}, {self.color}, {self.year}, {self.precio},({self.aceleracion}),{self.desplazamiento}"


c = auto("honda","rojo",2022,25000,40)

print(c)
c.acelerar()
c.acelerar()
c.acelerar()

print(c)
c.retroceder()
print(c)



