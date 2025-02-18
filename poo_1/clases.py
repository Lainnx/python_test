class Persona():    #la clase principal no necesita parentesis, son optativos, cuando haya herencia si que necesitan
    """ 
   Propiedades de una clase  
    """
    # nombre = None   #atributos de la clase
    # apellido = None   COMO ESTAMOS CREANDO UN CONSTRUCTOR ESTO NO LO NECESITAMOS
    # funcion = None

    #MÉTODOS
    def __init__(self, nombre1, apellido1, funcion1):       #método constructor, crea un objeto con los atributos que se consideren imprescindibles
                                                    #con este metodo se instancia, se paasa de la plantilla a un objeto con valores
                                                    #se usa con objetos que vayas a crear
                                                    #self hace referencia a esa instancia en concreto que se esta creando, apunta a ella
                                                    #plantilla->instancia->realidad
                                                    #clase--------------->objeto
                                                    #nombre---------------Peter
                                                    #apellido-------------Parler
        self.nombre = nombre1   #Método de instancia
        self.apellido = apellido1                   #nombre y nombre1 pueden ser iguales per no tiene que serlo, nombre1 tiene que ser el que esta en el __init__(nombre1)
        self.funcion = funcion1
    
    def __str__(self):   #para que cuando print(Objeto) se haga print de las propiedades(en el formato que se defina),a medida que se añaden propiedades hay que actualizar
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Funcion: {self.funcion}"
    
    #POLIMORFISMO, dentro de una clase puede haber una funcion llamada len(), ésta solo operará con objetos Persona. aunque se llaman igual pueden tener funciones distintas
                #puede haber algo que este en diferentes tipos de objetos y se llamé igual

    #Herencia: las propiedades de arriba pasan abajo
        #en python hay herencia múltiple, que los de abajo hereden de 2 o más, si hay demasiadas clases y/o relaciones el modelo falla (3,4+)
        

#un objeto es la instancia de una clase, cuando el objeto se crea se llama instancia

# persona_1 = Persona()   #objeto de tipo Persona
# # print(type(persona_1))  #Persona
# persona_1.nombre = "Peter"
# print(persona_1.nombre)     #en python no existen atributos privados o protegidos

persona_1 = Persona("Peter","Parker","alumno")
persona_1.nombre = "Pol"    #los objetos son mutables
print(persona_1.nombre)
print(persona_1)    #objeto de tipo Persona
