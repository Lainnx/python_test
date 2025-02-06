#INTRO DICCIONARIOS

#ALUMNO
#Nombre
#Apellido
#Edad
#Direccion
#Asignaturas está matriculado

# Con listas no es viable puede guardar informacion compleja
# alumnos = ["Pepe","Garcia",27,"calle xx",["Python","JS"]]

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