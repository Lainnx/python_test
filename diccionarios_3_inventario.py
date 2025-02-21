""" 
Crea un programa que utilize un diccionario para almacenar informacion de un inventario de productos

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualquiera.

Mostrar ahora todos los productos y sus cantidades
 """

# lista_productos = []            #como se añaden cosas nuevas a un diccionario¿?¿?¿
# lista_nombres = []              #https://www.digitalocean.com/community/tutorials/python-add-to-dictionary

# menu = """1: Introducir nuevo item
# 2: Modificar cantidad
# 3: Mostrar toda la lista
# X: Salir """
# while True:
#     for producto in lista_productos:
#         lista_nombres.append(producto["nombre"])
#     print(menu)
#     opcion = input("opcion: ").lower()
#     match opcion:
#         case "1":
#             try:
#                 nombre = input("Introduce el nombre del nuevo item: ").lower()
#                 cantidad = int(input("Introduce una cantidad para el nuevo item: "))
#                 if nombre not in lista_nombres:
#                     lista_nombres.append(nombre)
#                     dic ={"nombre":nombre,"cantidad":cantidad}
#                     lista_productos.append(dic)
#                 else:
#                     print("Este producto ya existe. Opcion 2 para modificar cantidad")
#             except ValueError:
#                 print("La cantidad tiene que ser un numero entero.")
#         case "2":
#             try:
#                 nombre = input("Introduce el nombre del producto del que quieres modificar la cantidad: ").lower()
#                 for dic in lista_productos:
#                     if dic["nombre"]==nombre:
#                         print(f"Cantidad actual: {dic["cantidad"]}")
#                         cantidad_nueva = int(input("Introduce la nueva cantidad (a sumar o restar)"))
#                         dic["cantidad"]+=cantidad_nueva
#                         print(f"Cantidad nueva: {dic["cantidad"]}")
#             except ValueError:
#                 print("La cantidad tiene que ser un numero entero.")
#         case "3":
#             for dic in lista_productos:
#                 print(f"Nombre: {dic["nombre"]} - {dic["cantidad"]}")
#         case "x":
#             print("Saliendo del programa.")
#             break
#         case _:
#             print("Opcion no reconocida.")

########solucion profe
inventario = {"manzanas":10,"peras":15,"kiwis":5,"limones":4,"naranjas":7}     #1a parte: crear un diccionario con 5 elementos

inventario["piñas"] = 3            #2o parte: añadir 2 productos 
                                    #Asi se añaden cosas en un dic, por la clave, no hay que preocuparse por la posicion
inventario["tomate"] = 5
print(inventario)
                            #3a parte: actualizar cantidades/ modificar
inventario["naranjas"] = 4 #se sustitye el valor
inventario["kiwis"] += 5   #se suma a la cantidad existente/ incrementar

print(inventario)
                            #4a parte: Quitar cosas del diccionario
#inventario.popitem()    #quita el ultimo que se ha puesto sin preguntar qual es   , si sale u cubo en el menu drop es que va con ()
fruta = inventario.pop("peras")     #.pop("clave) **quita del diccionario la clave indicada y lo puede guardar en una variable(como en el pop de listas)
                                    #solo guarda el valor, no crea un diccionario nuevo
print(inventario, fruta)
print(inventario.keys())
inventario.popitem()        #pop quita el ultimo por defecto
print(inventario)                   #.sort() modifica la lista
print(sorted(inventario, reverse = True))       #sorted() ordena pero no modifica, para mostrar informacion
for producto in sorted(inventario):             #hacen lo mismo +o-
    print(f"producto: {producto}")