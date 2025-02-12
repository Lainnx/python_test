#Funciones

# def sumar():          #Estado de declaracion, no  se ejecuta
#     print(1+2)        #Para poder llamar una funcion tiene que estar cargada en memoria ANTES

# sumar()               #llamada/invocación (ejecuta la funcion)

# def sumar():
#     return 1+2          #devuelve, hay que asignarlo

# x = sumar()
# print(x) #o print(sumar())

# def sumar(a,b):         #a y b son argumentos, se pasan a la funcion cuando se llama
#     return a+b          #En la declaración lo que hay en los parentesis son los PARAMETROS
                         
# print(sumar(3,7))       #En la ejecución/invocación lo que hay en los parentesis son ARGUMENTOS
# print(sumar(3.7,7.3))
# print(sumar("Hola ","y adiós"))

# resultado = sumar(2,3)  #se asigna

#Ejempplos de funciones:
#-- para ver si un numero es primo o no
#-- para corregir nombres mal escritos
#-- para calcular días, horas, etc de una cantidad de segundos
#-- para calcular los días qie faltan para una fecha

# def prueba_variables():           #en python todas las variables son globales menos las que están declaradas dentro de funciones
#     variable = "Soy una prueba"   #VENTAJA? -- la función cuando finaliza se encarga de limpiar la memoria

# print(variable)                   #variable no existe fuera de la funcion

# def return_test():
#     a=0       
#     return f"se pueden retrun formatos{a}"    #se puede hacer return a formatos, para print(return_test())

""" 
def add_user(lista_usuarios, new_user):
    usuario_nuevo = {"nombre":new_user,"visitas":0}     
    lista_usuarios.append(usuario_nuevo) 
    lista_exist.append(usuario_nuevo["nombre"]) 
    return f"Usuario {new_user} añadido correctamente"      #en vez de todo eso podemos poner print(lista_usuarios, new_user), y a parte de imprir ejecuta
"""

#valor por defecto en parametros                      -|-       #VALOR POR DEFECTO tiene que estar después de los que no estan por defecto, sino daría error
# def mostrar_datos_alumno(nombre, apellido, becado = False):    #funciones se corresponden con acciones, RECOMENDADO nombrarlas con verbos
#     if becado:
#         becado = "Sí"
#     else:
#         becado = "No"
#     return f"¿El alumno {nombre} {apellido} tiene beca? --> {becado}" 

# alumno_1 = mostrar_datos_alumno("Anna","Garcia")
# print(alumno_1)                                     #beca false
# alumno_2 = mostrar_datos_alumno("Joan","pou",True)
# print(alumno_2)                                     #beca True

#una funcion que sume qualquier cantidad de numeros que le demos como argumento
#sumar(1,2)         #3
#sumar(3,4,5)       #12
#sumar(6,4,5,3)     #28
#se puede con una lista, pero python tiene una forma de hacer una funcion que acepte cualquier cantidad de argumentos

# def sumar(*argv):   #argv ~ argumento variable (puede ser cualquier palabra pero argv por convenio), lo importante es el *
#     print(argv)

# sumar(1,2)      #(1,2)  son tuplas
# sumar(3,4,5)    #(3,4,5)
# sumar(6,23,4)   #(6,23,4)
