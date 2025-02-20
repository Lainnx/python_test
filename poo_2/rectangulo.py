""" 
Hay que crear una clase llamada Rectangulo

Necesitamos los métodos para obtener el area, el perimetro y la diagonal de la figura.

Cada uno en un metodo diferente

Lo probaremos con un rectangulo de lados 3 y 4
 """
import os
os.system("cls")

class Rectangulo():
    def __init__(self,base,h):
        self.base=base
        self.h=h
    
    def calculo_area(self):
        return self.base*self.h
    
    def calculo_perimetro(self):
        return 2*(self.base+self.h)
    
    def calculo_hipotenusa(self):
        return ((self.base**2)+(self.h**2))**(0.5)
    
rectangulo1 = Rectangulo(3,4)

area = rectangulo1.calculo_area()
perimetro = rectangulo1.calculo_perimetro()
hipotenusa = rectangulo1.calculo_hipotenusa()

print(f"A = {area}, P = {perimetro}, H = {hipotenusa}")