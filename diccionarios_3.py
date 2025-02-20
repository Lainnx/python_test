""" 
Crea un programa que utilize un diccionario para almacenar informacion de un inventario de productos

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualquiera.

Mostrar ahora todos los productos y sus cantidades
 """

lista_productos = []
lista_nombres = []

menu = """1: Introducir nuevo item
2: Modificar cantidad
3: Mostrar toda la lista
X: Salir """
while True:
    for producto in lista_productos:
        lista_nombres.append(producto["nombre"])
    print(menu)
    opcion = input("opcion: ").lower()
    match opcion:
        case "1":
            try:
                nombre = input("Introduce el nombre del nuevo item: ").lower()
                cantidad = int(input("Introduce una cantidad para el nuevo item: "))
                if nombre not in lista_nombres:
                    lista_nombres.append(nombre)
                    dic ={"nombre":nombre,"cantidad":cantidad}
                    lista_productos.append(dic)
                else:
                    print("Este producto ya existe. Opcion 2 para modificar cantidad")
            except ValueError:
                print("La cantidad tiene que ser un numero entero.")
        case "2":
            try:
                nombre = input("Introduce el nombre del producto del que quieres modificar la cantidad: ").lower()
                for dic in lista_productos:
                    if dic["nombre"]==nombre:
                        print(f"Cantidad actual: {dic["cantidad"]}")
                        cantidad_nueva = int(input("Introduce la nueva cantidad (a sumar o restar)"))
                        dic["cantidad"]+=cantidad_nueva
                        print(f"Cantidad nueva: {dic["cantidad"]}")
            except ValueError:
                print("La cantidad tiene que ser un numero entero.")
        case "3":
            for dic in lista_productos:
                print(f"Nombre: {dic["nombre"]} - {dic["cantidad"]}")
        case "x":
            print("Saliendo del programa.")
            break
        case _:
            print("Opcion no reconocida.")
    