""" 
Vamos a crear una clase llamada Persona, tendrá estos atributos:
-Nombre
-Apellido
-Ciudad
Crear el constructor y el método que muestra la informacion de la clase (print(objeto)->muestra caracteristicas)

También habrá una clase hija llamada Cliente.
Tendrá además los atributos:
-dni
-compras

Cuando se muestre el objeto deben aparecer todos los atributos

Hay que crear un método llamado compras_realizadas que tenga esta salida:
El cliente Fulanito ha comprado xx.xx €
 """
import os
os.system("cls")

class Persona():                                #como es la clase principal no es imprescindible poner () pero buena practica
    def __init__(self,nombre,apellido,ciudad):  #__init__(self,nombre:str,apellido:str,ciudad:str) se puede, NOTACION INFORMATIVA, (cuando pasas el cursor por encima)
        self.nombre=nombre
        self.apellido=apellido
        self.ciudad=ciudad
    
    def __str__(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCiudad: {self.ciudad}")   #aqui print porque si fuera return al ejecutar desde hijo finaliza funcion

class Cliente(Persona):                 #si no tiene constructor usa el de la clase padre, lo mismo con el __str__
    def __init__(self,nombre,apellido,ciudad,dni,compras):
        # self.nombre=nombre            #se puede hacer sobreescribiendo los atributos del padre(no optimo)
        # self.apellido=apellido
        # self.ciudad=ciudad                        #super va a buscar la funcion del ancestro directo
        super().__init__(nombre,apellido,ciudad)    #como este init ya esta construido en el padre ira a buscar las propiedades en el padre
        self.dni=dni                                #el self aqui no hace falta poruqe lo hemos puesto antes
        self.compras=compras

    def __str__(self):
        super().__str__()   #llama la funcion del padre
        return f"DNI: {self.dni}\nCompras:{self.compras} €"
    
    def compras_realizadas(self):
        return f"El cliente {self.nombre} {self.apellido} ha comprado {self.compras} €"
    
# persona1 = Persona("N","A","C") #declara objeto Persona
cliente1 = Cliente("N","A","C","123",63.23)     #declara objeto Cliente

# print(persona1) #constructor Persona
print(cliente1) #
# print(Cliente.compras_realizadas(cliente1))    #funcion compras_realizadas, asocia persona1 y cliente1
print(cliente1.compras_realizadas())