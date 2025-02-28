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
    def __init__(self,nombre,apellido):#constructor de clase Lector
        self.nombre=nombre
        self.apellido=apellido
        self.lista_prestamos=[]     #lista con los libros que tiene prestado cada lector

    def __str__(self):
        ret = f"Nombre: {self.nombre}, Apellido: {self.apellido}\n"
        if self.lista_prestamos:
            for item in self.lista_prestamos:
               ret += (item.titulo + " ")
        return ret


class Libro():
    def __init__(self,nombre_autor,apellido_autor,titulo):  #constructor de clase Libro
        self.nombre_autor=nombre_autor
        self.apellido_autor=apellido_autor
        self.titulo=titulo
        self.ejemplares=0       #numero de ejemplares de cada libro que hay en la biblioteca, = 0 al principio, luego hago siempre += o -= para actualizar este numero

    def __str__(self):
        ret = f"Nombre autor: {self.nombre_autor} {self.apellido_autor}\nTitulo: {self.titulo}. {self.ejemplares} ej."
        return ret

class Biblioteca():
    def __init__(self,nombre,direccion):    #constructor de clase Biblioteca
        self.nombre=nombre
        self.direccion=direccion
        self.lista_lectores=[]          #declaracion de lista de lectores (vacía al principio) 
        self.lista_libros=[]            #declaracion de lista de libros (vacía al principio)


    def agregar_lector(self,lector):    #funcion que agrega lectores a la biblioteca
        flag = False                    #esta variable indicara si hay que añadir o no a la lista de lectores(porque sino en el for se añaden mas de una vez)
        if self.lista_lectores:         #si la lista de lectores tiene elementos dentro
            # print("lista lectores",self.lista_lectores)
            for item in self.lista_lectores:    #iteramos sobre la lista de lectores
                # print(item.nombre,lector.nombre)
                if item.nombre.lower() == lector.nombre.lower() and item.apellido.lower() == lector.apellido.lower():   #si el nombre y el apellido del lector que queremos añadir == al nombre y ap. del lector en lista_lectores
                    print( f"Este lector ya existe en la base de datos")                                                #es que ese lector ya existe en la lista, informamos y salimos de la funcion con return 0
                    return 0    #flag = False aqui no hace falta porque return 0 ya sale de la función
                else:
                    # lis_lector = lector
                    flag = True     #si el lector que queremos añadir no coincide con el de la lista (en una iteración) flag sera true, y si no esta en la lista nunca entrara en el if de arriba, por lo que cuando salga del for entrara en la siguiente condicion
            if flag:                #si flag es True(el nombre que queremos añadir no esta ya en la lista lectores)
                self.lista_lectores.append(lector)  #lo añadimos a la lista
                print( f"Lector agregado {lector.nombre}")  #e informamos de ello al usuario
                return 0
                    
        else:                           #si la lista no tiene elementos dentro añade el lector actual directamente, no hace falta comprovar porque es el primero
            self.lista_lectores.append(lector)
            print( f"Lector agregado {lector.nombre} {lector.apellido}")


    def mostrar_lectores(self):     #muestra todos los lectores registrados en la biblioteca
        # print(self.lista_lectores)
        for lector in self.lista_lectores:      #itera sobre la lista de lectores e imprime cada elemento con cierto formato
            print(f"Nombre: {lector.nombre} Apellido: {lector.apellido} - {lector.lista_prestamos}")   #si return se termina la funcion por eso solo imprmia 1, si no return aqui no prints abajo
        

    def agregar_libro(self,libro:Libro,ejemplares:int):   #funcion para agregar libros a la biblioteca
        if self.lista_libros:           #si la lista de libros tiene elementos dentro (no se puede iterar sobre una lista vacía)
            flag = False
            for item in self.lista_libros:      #for porque tiene que comprovar si coincide con alguno o no
                if item.nombre_autor.lower() == libro.nombre_autor.lower() and item.apellido_autor.lower() == libro.apellido_autor.lower() and item.titulo.lower() == libro.titulo.lower(): #si el libro es el mismo
                    item.ejemplares += ejemplares   #suma los ejemplares nuevos a los existentes
                    print(f"{ejemplares} ejemplares añadidos a {item.titulo}.") #el for se tiene que ejecutar todas las veces que sea necesario, hasta que acabe o hasta que
                    return 0                                                    #encuentre el que cumple la cond. del if(en cuyo caso sale de la funcion directamente)
                else:                                                           #sino flag = True para que se ejecute el resto del codigo
                    flag = True                                                 #
            if flag:                        
                libro.ejemplares += ejemplares  
                self.lista_libros.append(libro)
                print(f"Libro agregado: {libro.titulo}, {libro.ejemplares} ej. disp.")
        else:                               #si la lista esta vacía añade el primer elemento (como es el primero no hace falta comprovar si ya está dentro o no)
            libro.ejemplares += ejemplares  #suma el numero de ejemplares nuevo al existente(la variable empieza con valor 0)
            self.lista_libros.append(libro) #añade el libro a la lista de libros
            print(f"Libro agregado: {libro.titulo}, {ejemplares} ej. disp.")    #informa al usuario
    

    def mostrar_libros(self):   #muestra los libros que hay en la lista de la biblioteca
        # print("3",self.lista_libros)
        # for libro in self.lista_libros: #itera sobre la lista de libros
        #     print(f"Titulo: {libro.titulo} N.Aut: {libro.nombre_autor} A.Aut: {libro.apellido_autor} - {libro.ejemplares} disponibles.")    #hace print de los libros con un formato
        max_col_1 = 10
        max_col_2 = 15
        max_col_3 = 10
        lista1 =[0,"|",0,"|",0]
        print(f"Libros de la {self.nombre}")
        print(f"Autor     |Titulo         |Ejemplares")
        print(f"--------------------------------------")
        for item in self.lista_libros:
            nombre_a=""
            nombre_autor = item.nombre_autor + item.apellido_autor
            if len(nombre_autor)>max_col_1:    #siempre que pase esto pondremos los ...    COLUMNA 1
                resta1 = len(nombre_autor)-max_col_1   #diferencia
                nombre_a = nombre_autor[:-resta1]
                resta11 = len(nombre_a)-max_col_1-3
                print(nombre_a[:resta11]+"."*3+"|",end="")     #no hacer prints, guardar en variables i al final prind, hacer por columnas
            elif len(nombre_autor)<=max_col_1:
                print(f"{nombre_autor: <{max_col_1}}|",end="")    #intercala espacios en lugar de puntos .<8

            if len(item.titulo)>max_col_2:              #COLUMNA 2
                resta2 = len(item.titulo)-max_col_2
                titulo_a = item.titulo[:-resta2]
                resta22 = len(titulo_a)-max_col_2-3
                print(titulo_a[:resta22]+"."*3+"|",end="")
            elif len(item.titulo)<=max_col_2:
                print(f"{item.titulo: <{max_col_2}}|",end="")
            
            if len(str(item.ejemplares))>max_col_3:              #COLUMNA 3
                resta3 = len(str(item.ejemplares))-max_col_3
                ejem_a = item.ejemplares[:-resta3]
                resta33 = len(ejem_a)-max_col_3-3
                print(ejem_a[:resta33]+"."*3+"|",end="\n")
            elif len(str(item.ejemplares)) <= max_col_3:
                print(f"{item.ejemplares: <{max_col_3}}|",end="\n")

    
    def buscar_libros(self,nombre_autor,apellido_autor,titulo): #busca libros en la lista de libros
        flag = False    #como uso un for flag para comprovar si se cumple una condicion sin que se ejecute el codigo n veces
        for item in self.lista_libros:      #itera sobre lista de libros
            if item.nombre_autor.lower() == nombre_autor.lower() and item.apellido_autor.lower() == apellido_autor.lower() or item.titulo.lower() == titulo.lower():    #si el libro es el mismo es que existe
                flag = True     #flag True para ejecutar el codigo
        if flag:    #si flag sigue siendo false es que el libro no esta en la lista(nunca se cumplió la condicion de arriba)
            print(f"El libro {titulo.title()} está en {self.nombre}")   #si es True es que si que está en la lista
        else:
            print(f"El libro {titulo.title()} no está en {self.nombre}")

    
    def reservar_libros(self,nombre_libro:str,lector:Lector):   #funcion para reservar libros
        flag = False    #otra vez, al usar un for uso flag para ccomprovar condiciones
        for libro in self.lista_libros: #itero sobre lista libros
            if libro.titulo == nombre_libro:    #cuando el nombre del libro que esta en la biblioteca sea igual al libro que se esta solicitando
                if libro.ejemplares > 0:    #si hay ejemplares disponibles para ser prestados
                    libro.ejemplares -= 1   #uno menos(el que se llevan)
                    lector.lista_prestamos.append(libro)    #se añade el libro a la lista de prestamos del usuario, hay un registro en cada objeto Lector con los libros que tienen prestados
                    print(f"Reserva realizada de: {libro.titulo} por {lector.nombre} {lector.apellido}.")   #y se informa
                    print(f"Quedan {libro.ejemplares} ejemplares del libro {libro.titulo}.")
                    return 0    #si se ejecuta el codigo de arriba la funcion ya ha cumplido su funcion por lo que return 0 la termina
                else:
                    print(f"No quedan ejemplares de {libro.titulo} para prestar.")  #si no quedan ejemplares disponibles se informa y se termina la funcion
                    return 0
            else:   #este else se ejecutará cuando el nombre del libro a reservar no coincida con el de la iteracion del for, en cuyo caso flag = True
                flag = True
        if flag:    #si flag persiste siendo True querra decir que el codigo nunca ha entrado en los ifs de arriba(los return 0 terminan la funcion) por lo que querra decir que el libro no existe en la lista de libros de la biblioteca
            print(f"El libro {nombre_libro} no esta en el registro de la biblioteca {self.nombre}.")
            
    
    def devolver_libros(self,nombre_libro:str,lector:Lector):   #funcion para devolver libros
        flag = False    #lo mismo, como uso for uso una flag para comprobar
        if lector.lista_prestamos:  #si la lista de prestamos del lector tiene algun elemento dentro(tiene prestado algun libro)
            for item in lector.lista_prestamos: #itera sobre la lista de prestamos del objeto lector
                if item.titulo == nombre_libro: #si el nombre del libro a devolver coinde con el nombre del libro iterado
                    self.agregar_libro(item,1)  #el libro que se devuelve, 1 ejemplar
                    lector.lista_prestamos.remove(item) #se elimina de la lista de prestamos del lector
                    print(f"Libro {item.titulo} devuelto con exito.")   #se informa
                    return 0    #termina la funcion
                else:   #
                    flag = True    
        else:   #sino tiene elementos dentro no tiene nada que devolver
            print(f"Este lector no tiene libros que devolver.")
            return 0
        if flag:    #si flag persiste y cuando llega aqui es True es que nunca ha entrado en el codigo de arriba, lo que quiere decir que el libro que se esta intentando devolver no esta en la lista
            print(f"El libro que estas intentando devolver no pertenece a esta biblioteca.")
            

lec1=Lector("nn","aa")
lec2=Lector("rr2","aa2")
libro1=Libro("nombreeeeeeeeee","apellidoqqqqqqqqqqqqqqqqqqqqqq1","tituqqqqqqqqqqqqqqqqqlo1")
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
