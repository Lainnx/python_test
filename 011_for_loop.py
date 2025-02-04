#FOR LOOP

nombres = ["Pol","Pau","Luis","Juan","Pablo","paco"] #nombre de listas buena idea en PLURAL
edades = [25,30,35,40,45,28,24,65,36]

#Ejercicio 1: mostrar los nombres que empiezan por p
"""
#print(type(nombres))       #si declaro sin [] se crea una tupla
#print(type(nombres))       #type list - no se puede hacer .lower() en una lista
for i in nombres:           #nombre i buena idea no i sino SINGULAR
    #print(type(i))         #type string
    i = i.lower()           #.lower() en una string
    if i[0] == "p":
        print(i.capitalize())
#print(i)    #se queda con el ultimo valor asignado en el for

check = "P"

for nombre in nombres:
    #if nombre[0].lower() == check.lower():
    #    print(nombre.capitalize())
    if nombre.lower().startswith(check.lower()):    #se pueden concatenar funciones, primero hace el lower() al nombre y luego el startswith()
        print(nombre.capitalize())
"""
#Ejercicio 2: mostrar los numeros de esades que empiezan por 2 y la suma de estos
z = 0
check = 2
"""
for i in edades:
    x = str(i)
    #if x[0]=="2":
    #    print(i)
    if x.startswith("2"):
        print(i)
        z += i
print("suma :", z)
"""
"""
for edad in edades:
    if str(edad).startswith(str(check)):    #se hace str de i i mira si empieza por check(convierte a string primero, check es int)
        print(edad, end =" ")               #end = " " para que en lugar de \n finalize con un espacio
        z += edad
print("\nsuma :", z)                        #se imprime despues de un espacio, la ultima iteracion del for pone un " ", luego vuelve a \n
print("se imprime en la siguiente linea")   #se imprime en la siguiente linea   

#Ejercicio 3: mostrar: la suma de los valores es X, hay X elementos y el promedio es:
a = 0
for edad in edades:     #sum(edades)
    a += edad
promedio = a/len(edades)
print("suma :", a)
print(f"hay {len(edades)} elementos")
print("promedio :", promedio)
#print(sum(edades))
"""
"""
checkn="luis" #alba
k = 0

for i in nombres:       #for checkn in nombres -- ya itera buscando checkn¿?
    print(i)
    if i.lower() == checkn.lower():
        print(f"{checkn.capitalize()} esta en la lista")
        break                                               #para romper/finalizar el bucle, ha encontrado el nombre una vez, esta en la lista, para de buscar
else:                                                       #cuando no hay un break se ejecuta el else, SOLO en el caso que no haya un break
    print(f"{checkn} no esta en la lista")
"""

#Quiero saber que nombres de la lista contienen la letra "o"
"""
nombres_con_o =[]                       #inicializa la lista vacía
                                        #i = nombre
for i in nombres:
    indice = nombres.index(i)           #pide el indice, en otros lenguajes i++, aqui i (nombre) realmente no es un numero, es un miembro de la lista
    #if i.lower().count("o") >= 1:
    #    print(i)
    if "o" in i.lower():                #busca si "o" esta en el nombre
        print(f"{indice+1}, {i}")       #indice+1 porque la maquina emieza a contar por 0
        nombres_con_o.append(i)         #pone el nombre al final de la lista vacía
#print(nombres_con_o)
"""
#RANGE(X)   crea un rango de valores (X-1)
#print(list(range(10)))  #range es un tipo de dato que no tiene salida, casting a lista para que print lo entienda

#for i in range(10):
#    print(i, end =" ")

for index in range(len(nombres)):       #trabajando con indices como en otros lenguajes
    print(f"{index} {nombres[index]}")
