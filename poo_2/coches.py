""" 
Crear una clase llamada Coche
Tendrá los siguientes atributos:
-marca
-color
-combustible
-cilindrada

Crear la función __init__ con los parámetros anteriores.

Crear otra función llamada mostrar_caracteristicas que muestre todos los detalles anteriores en un único mensaje

Crear la función __str__ que tendrá como salida la marca y el color

Con eso crearemos un objeto Coche, con estos calores:
-Opel
-Rojo
-Eléctrico
-1.8

Ejecutar las funciones que acabas de crear
 """
import os
os.system("cls")

class Coche():                                                  #clase BUENA PRACTICA EMPEZAR CON MAYUSCULA
    def __init__(self,marca,color,combustible,cilindrada):      #Constructor
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Color: {self.color}"
    
    def mostrar_caracteristicas(self):
        return f"""Marca: {self.marca}\nColor: {self.color}\nCombustible: {self.combustible}\nCcs: {self.cilindrada}"""

carro = Coche("Opel","Rojo","Eléctrico",1.8)    #instancia objeto Coche y se inicia con las caracteristicas

print (carro)                                   #print de objeto Coche devolvera en __str__
print (Coche.mostrar_caracteristicas(carro))    #llama la funcion mostrar_caract(necesita un objeto Coche para ejecutar)
