"""
Programación Orientada a Objetos: Biblioteca

El programa debe crear las siguientes clases con sus métodos:

    Clase Lector, que se construirá con nombre y apellido

    Clase Libro, que se construirá con nombre_autor, apellido_autor,
    y título

    Clase Biblioteca, que se construirá con nombre y dirección
    Esta clase dispondrá de los siguientes métodos:
    - agregar_lector: agrega un lector a la biblioteca
    - mostrar lectores
    - agregar_libro: agrega un libro a la biblioteca,
        indicando los ejemplares disponibles
    - buscar_libro: busca un libro en la biblioteca, 
        indicando si lo tiene o no
    - mostrar libros de la biblioteca


"""
import os
os.system("cls")

class Lector():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido



class Libro():
    def __init__(self,nombre_autor,apellido_autor,titulo):
        self.nombre_autor=nombre_autor
        self.apellido_autor=apellido_autor
        self.titulo=titulo
        self.ejemplares=0



class Biblioteca():
    def __init__(self,nombre,direccion):
        self.nombre=nombre
        self.direccion=direccion
        self.lista_lectores=[]
        self.lista_libros=[]


    def agregar_lector(self,lector):
        if self.lista_lectores:
            # print("lista lectores",self.lista_lectores)
            for item in self.lista_lectores:
                # print(item.nombre,lector.nombre)
                if item.nombre.lower() == lector.nombre.lower() and item.apellido.lower() == lector.apellido.lower():
                    print( f"Este lector ya existe en la base de datos")
                else:
                    # lis_lector = lector
                    self.lista_lectores.append(lector)
                    print( f"Lector agregado {lector.nombre}")
        else:
            self.lista_lectores.append(lector)
            print( f"Lector agregado {lector.nombre} {lector.apellido}")


    def mostrar_lectores(self):
        # print(self.lista_lectores)
        for lector in self.lista_lectores:
            print(f"Nombre: {lector.nombre} Apellido: {lector.apellido}")   #si return se termina la funcion por eso solo imprmia 1, si no return aqui no prints abajo
        

    def agregar_libro(self,libro,ejemplares):
        if self.lista_libros:
            flag = False
            for item in self.lista_libros:      #for porque tiene que comprovar si coincide con alguno o no
                if item.nombre_autor.lower() == libro.nombre_autor.lower() and item.apellido_autor.lower() == libro.apellido_autor.lower() and item.titulo.lower() == libro.titulo.lower():
                    item.ejemplares += ejemplares
                    print(f"{ejemplares} ejemplares añadidos a {item.titulo}.") #el for se tiene que ejecurar todas las veces que sea necesario, hasta que acabe o hasta que
                    return 0                                                    #encuentre el que cumple la cond. del if(en cuyo caso sale del bucle)
                else:
                    flag = True
            if flag:
                libro.ejemplares += ejemplares
                self.lista_libros.append(libro)
                print(f"Libro agregado: {libro.titulo}, {libro.ejemplares} ej. disp.")
        else:
            libro.ejemplares += ejemplares
            self.lista_libros.append(libro)
            print(f"Libro agregado else1 : {libro.titulo}, {ejemplares} ej. disp.")
    

    def mostrar_libros(self):
        # print("3",self.lista_libros)
        for libro in self.lista_libros:
            print(f"Titulo: {libro.titulo} N.Aut: {libro.nombre_autor} A.Aut: {libro.apellido_autor} - {libro.ejemplares} disponibles.")

    
    def buscar_libros(self,nombre_autor,apellido_autor,titulo):
        flag = False
        for item in self.lista_libros:
            if item.nombre_autor.lower() == nombre_autor.lower() and item.apellido_autor.lower() == apellido_autor.lower() or item.titulo.lower() == titulo.lower():
                flag = True
        if flag:
            print(f"El libro {titulo.title()} está en {self.nombre}")
        else:
            print(f"El libro {titulo.title()} no está en {self.nombre}")

    
    def reservar_libros(self,libro):
        pass
            

# lec1=Lector("nn","aa")
# lec2=Lector("rr2","aa2")
libro1=Libro("nombre1","apellido1","titulo1")
libro2=Libro("nombre2","apellido2","Tilulo2")
bib1=Biblioteca("nombiblio","direcciobibilio")
# bib1.agregar_lector(lec1)
# bib1.agregar_lector(lec2)
bib1.agregar_libro(libro1,3)
bib1.agregar_libro(libro2,5)
bib1.agregar_libro(libro2,2)
bib1.agregar_libro(libro1,3)
# bib1.mostrar_lectores()
bib1.mostrar_libros()
# bib1.buscar_libros("nombre1","apellido1","titulo2")