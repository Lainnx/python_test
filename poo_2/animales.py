class Animal():     #en general nombre clase primera mayus
    def __init__(self, especie1):   #constructor
        self.especie = especie1
    def __str__(self):
        return f"la especie es: {self.especie}"
    
class Perro(Animal):    #Perro hereda de Animal, pero Animal no de Perro
    def sonido(self):    #self poruqe depende del objeto
        print("Bup")

tortuga = Animal("Tortuga") #indicamos la especie (requerido por el constructor)

                #| hay que añadir la especie al añadir el constructor en el padre
milu = Perro("Perro")      #como no hemos indicado constructor se queda así
milu.sonido()       #Bup

class Gato(Animal):
    def sonido(self):   #cada animal ejecuta la funcion de manera diferente, entonces hay que declararla cada vez
        print("Miau")

mishi = Gato("Siamés")

print(Perro.__bases__)  #dice el ancestro directo, (Animal)
print(Animal.__subclasses__())    #descendientes directos (Perro y Gato)

print(milu) #el __str__ está en Animal, Perro tambien lo puede usar aunque no lo tenga
            #polimorfismo: se puede tener la misma funcion en diferentes sitios
            #encapsulamiento: se puede tener una variable llamada igual en diferentes sitios

