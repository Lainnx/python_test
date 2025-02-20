'''
Crea una clase llamada Vehiculo.

En su constructor incluye marca, modelo y año de construcción.

Dos métodos también:
-- arrancar, con el mensaje "El vehículo XX modelo YY ha arrancado"
-- detener, con el mensaje "El vehículo XX modelo YY se ha detenido"

Luego, dos clases hijas: Coche y Moto

La clase Coche tiene dos atributos propio: numero de puertas y AC (verdadero o falso).
y también un método propio: abrir_maletero, que
devuelve este mensaje: "El maletero del [marca] [modelo] está abierto"

La clase Moto tiene un método propio: revisar_seguridad, devuelve este mensaje:
"Si circulas en motocicleta debes llevar casco"
'''
class Vehiculos():
    def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año

    def arrancar(self):
        return f"El vehiculo {self.marca} modelo {self.modelo} ha arrancado"
    def detener(self):
        return f"El vehiculo {self.marca} modelo {self.modelo} se ha detenido"
    
class Coches(Vehiculos):
    def __init__(self,marca,modelo,año,puertas,AC:bool):
        super().__init__(marca,modelo,año)
        self.puertas=puertas
        self.AC=AC

    def abrir_maletero(self):
        return f"El maletero del {self.marca} {self.modelo} está abierto"
    
class Motos(Vehiculos):
    # def __init__(self,marca,modelo,año):  #si no hay atributos nuevos no hace falta cojer del super(), hereda directamente los atributos del padre
    #     super().__init__(marca,modelo,año)    #si hay que poner atributos nuevos ahí si que se usa super para ir a buscar los atributos del padre
    
    def revisar_seguridad(self):
        return f"Si circulas en motocicleta debes llevar casco"
    
coche = Coches("Marca","Modelo",1995,4,False)
print(coche.arrancar())
print(coche.detener())
print(coche.abrir_maletero())

moto = Motos("Marca1","Modelo1",2000)
print(moto.arrancar())
print(moto.detener())
print(moto.revisar_seguridad())