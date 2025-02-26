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
        self.lista_prestamos=[] #lista con los libros que tiene prestado cadad lector

    def __str__(self):
        ret = f"Nombre: {self.nombre}, Apellido: {self.apellido}\n"
        if self.lista_prestamos:
            for item in self.lista_prestamos:
               ret += (item.titulo + " ")
        return ret


class Libro():
    def __init__(self,nombre_autor,apellido_autor,titulo):
        self.nombre_autor=nombre_autor
        self.apellido_autor=apellido_autor
        self.titulo=titulo
        self.ejemplares=0

    def __str__(self):
        ret = f"Nombre autor: {self.nombre_autor} {self.apellido_autor}\nTitulo: {self.titulo}. {self.ejemplares} ej."
        return ret

class Biblioteca():
    def __init__(self,nombre,direccion):
        self.nombre=nombre
        self.direccion=direccion
        self.lista_lectores=[]
        self.lista_libros=[]


    def agregar_lector(self,lector):
        flag = False
        if self.lista_lectores:
            # print("lista lectores",self.lista_lectores)
            for item in self.lista_lectores:
                # print(item.nombre,lector.nombre)
                if item.nombre.lower() == lector.nombre.lower() and item.apellido.lower() == lector.apellido.lower():
                    print( f"Este lector ya existe en la base de datos")
                    flag = False
                    return 0
                else:
                    # lis_lector = lector
                    flag = True
            if flag:
                self.lista_lectores.append(lector)
                print( f"Lector agregado {lector.nombre}")
                return 0
                    
        else:
            self.lista_lectores.append(lector)
            print( f"Lector agregado {lector.nombre} {lector.apellido}")


    def mostrar_lectores(self):
        # print(self.lista_lectores)
        for lector in self.lista_lectores:
            print(f"Nombre: {lector.nombre} Apellido: {lector.apellido} {lector.lista_prestamos}")   #si return se termina la funcion por eso solo imprmia 1, si no return aqui no prints abajo
        

    def agregar_libro(self,libro,ejemplares):
        if self.lista_libros:
            flag = False
            for item in self.lista_libros:      #for porque tiene que comprovar si coincide con alguno o no
                if item.nombre_autor.lower() == libro.nombre_autor.lower() and item.apellido_autor.lower() == libro.apellido_autor.lower() and item.titulo.lower() == libro.titulo.lower():
                    item.ejemplares += ejemplares
                    print(f"{ejemplares} ejemplares añadidos a {item.titulo}.") #el for se tiene que ejecurar todas las veces que sea necesario, hasta que acabe o hasta que
                    flag = False
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

    
    def reservar_libros(self,nombre_libro:str,lector:Lector):
        flag = False
        for libro in self.lista_libros:
            if libro.titulo == nombre_libro:    #cuando el nombre del libro que esta en la biblioteca sea igual al libro que se esta solicitando
                if libro.ejemplares > 0:
                    libro.ejemplares -= 1
                    lector.lista_prestamos.append(libro)
                    print(f"Reserva realizada de: {libro.titulo} por {lector.nombre} {lector.apellido}.")
                    print(f"Quedan {libro.ejemplares} ejemplares del libro {libro.titulo}.")
                    flag = False
                    return 0
                else:
                    print(f"No quedan ejemplares de {libro.titulo} para prestar.")
                    flag = False
                    return 0
            else:
                flag = True
        if flag:
            print(f"El libro {nombre_libro} no esta en el registro de la biblioteca {self.nombre}.")
            
    
    def devolver_libros(self,nombre_libro,lector:Lector):
        flag = False
        if lector.lista_prestamos:
            for item in lector.lista_prestamos:
                if item.titulo == nombre_libro:
                    self.agregar_libro(item,1)  #el libro que se devuelve, 1 ejemplar
                    lector.lista_prestamos.remove(item)
                    print(f"Libro {item.titulo} devuelto con exito: quedan {item.ejemplares}")
                    flag = False
                    return 0
                else:
                    flag = True    
        else:
            print(f"Este lector no tiene libros que devolver.")
            return 0
        if flag:
            print(f"El libro que estas intentando devolver no pertenece a esta biblioteca.")
            

lec1=Lector("nn","aa")
lec2=Lector("rr2","aa2")
libro1=Libro("nombre1","apellido1","titulo1")
libro2=Libro("nombre2","apellido2","Tilulo2")
libro3=Libro("Nombre3","apellido3","Titulo3")
bib1=Biblioteca("nombiblio","direcciobibilio")
bib1.agregar_lector(lec1)
bib1.agregar_lector(lec2)
bib1.agregar_lector(lec1)
bib1.agregar_libro(libro1,3)
bib1.agregar_libro(libro2,5)
bib1.agregar_libro(libro2,2)
bib1.agregar_libro(libro1,3)
bib1.agregar_libro(libro3,3)
bib1.mostrar_lectores()
bib1.mostrar_libros()
# bib1.buscar_libros("nombre1","apellido1","titulo2")
bib1.reservar_libros("titulo1",lec1)
bib1.mostrar_libros()
print(lec1)
bib1.mostrar_lectores()
bib1.devolver_libros("titulo1",lec1)
bib1.mostrar_libros()
print(lec1)