#INTRO DICCIONARIOS

#ALUMNO
#Nombre
#Apellido
#Edad
#Direccion
#Asignaturas está matriculado

# Con listas no es viable puede guardar informacion compleja
# alumnos = ["Pepe","Garcia",27,"calle xx",["Python","JS"]]
import os

alumnos = [["Pepe","Garcia",27,"calle xx",["Python","JS"]], ["Maria","Pons",22,"calle xx",["Python","JS"]]]   #array de arrays

for nombre, apellido, edad, direccion, asignaturas in alumnos:      #funcionaria pero todos estos elementos tiene que tener la misma longitud (en numero de elementos)
    print(f"El alumno {nombre} {apellido} de {edad} años ")         #se puede pero no es viable 

dic_alumno_1 = {"nombre": "Pepe", "edad": 22}  #LOS DICCIONARIOS CON {}, LAS LISTAS CON []
                                                #propiedades(entre comillas SIEMPRE), separadas por comas
dic_alumno_2 = {"nombre": "Maria","edad": 25}   #las claves tienen que ser ÚNICAS,no se puede poner nombre 2 veces
                                                #los diccionarios pueden ir dentro dearrays
mis_alumnos = [dic_alumno_1, dic_alumno_2]

#acceder a una propiedad del diccionario
print(type(dic_alumno_2["nombre"])) #string, el type de los nombres

print(mis_alumnos[0]["nombre"]) #Pepe - dic en primera posicion propiedad nombre

#son mutables
dic_alumno_2["nombre"] = "Anna" #se cambia la propiedad
print(dic_alumno_2)

#Actualizar diccionarios
dic_alumno_3 = {"nombre":"Pol", "beca":True}        #si la propiedad está cambiará el valor, y sino está se va a añadir
                                                    #si esta en el original pero en el otro no se va a mantener
dic_alumno_1.update(dic_alumno_3)
print(dic_alumno_1)                     #cambia el nombre a pol(dic3), la edad se mantiene i se añade beca

#Como iterar por un diccionario
for props in dic_alumno_1:  #print claves
    print(props)
print(dic_alumno_1.keys())  #imprime las llaves y las pone en un array
print(dic_alumno_1.values())#imprime los valores en un array

########################################################
os.system("cls")

#Diccionarios, los diccionarios son mutables
#El acceso al dato se prohibe medinte un identificador llamado "clave". Así: "clave": "valor",separados por "," la clave puede ser un string, un numero(no se suele hacer), una tupla,...
# {}
dic_1 = {}  #diccionario vacio  
list_1 = [] #lista vacia        || tienen caracter booleano

if not list_1:
    print("La lista esta vacia")

dic_1 = {"nombre": "Maria","apellido": "Callas","edad": 53} #puedes acceder por la clave en lugar del indice, no tienes que saber en que orden estan los datos
print(dic_1["nombre"])          #si busca así y no existe la clave da error y rompoe el codigo
# print(dic_1["direccion"])     #error porque no hay clave direccion
#mejor opcion
print(dic_1.get("nombre"))      #el get no rompe el codigo si no hay la clave,
print(dic_1.get("direccion"))   #None, no error

clave = "direccion"             #tambien se le puede poner un segundo argumento, un mensaje
print(dic_1.get(clave, f"la clave {clave} no existe en el diccionario")) #en lugar del none

#podemos iterar por lo que hay dentro
#iteracion directa
for propiedad in dic_1:
    print(propiedad)        #la iteracion da las claves

#iteracion especifica de claves
for propiedad in dic_1.keys():  #obtiene las claves
    print(propiedad)
#iteracion especifica de valores
for propiedad in dic_1.values():  #obtiene los valores
    print(propiedad)

#iteracion especifica de valores
for clave, valor in dic_1.items():  #obtiene las 2 cosas clave y valor, en ese orden 
    print(f"{clave} : {valor}")

#para añadir otro elemento (conjunto de clave y valor)
dic_1["pais"] = "Grecia"
print(dic_1)
#valores de la actualizacion
dic_actualizacion = {"ciudad": "Paris", "edad": 50}     

dic_1.update(dic_actualizacion)                         #modifica valores y añade cosas si no estan
print(dic_1)

