""" 
1 
Tenemos un sitio que registra los accesos de los usuarios.
Necesitamos un menú con estas opciones:
1. Añadiremos un usuario (si no existe ya)
    (si no existe ya)
2. Añadiremos una visita al usuario indicado
    (si el usuario no existe mostrar error)
3. Mostraremos las visitas del usuario que se decida
    (si el usuario no existe mostrar error)
4. Mostraremos las visitas de todos los usuarios
    (si no hay usuarios indicarlo)
X. Salir
"""

def no_user():
    print("Error: No existe el usuario indicado")

lista_usuarios = []

while True:
    print("Menu:")
    print("1. Añadir un usuario")
    print("2. Añadir una visita al usuario indicado")
    print("3. Mostrar las visitas del usuario que se decida")
    print("4. Mostrar las visitas de todos los usuarios")
    print("X. Para salir del programa")
    print(lista_usuarios)
    opcion = input("").strip().lower()

    match opcion:
        case "1":
            existe = 0
            new_user = input("Introduce el nombre del usuario que deseas añadir: ").strip().title()
            # usuario_nuevo = {"nombre":user,"visitas":0}
            if lista_usuarios:                                          #si no hay nada en la lista el for no tiene sobre qué iterar
                for user in lista_usuarios:
                    if user["nombre"] == new_user:
                        existe += 1
                        print(existe) 
                if existe == 0:
                    usuario_nuevo = {"nombre":new_user,"visitas":0}
                    lista_usuarios.append(usuario_nuevo) 
                    print(f"Usuario {new_user} añadido correctamente")
                else:
                    print("Ese usuario ya existe")
                    print("user: ",new_user)
                    # user["visitas"] += 1
            else:
                usuario_nuevo = {"nombre":new_user,"visitas":0}
                lista_usuarios.append(usuario_nuevo)
                print(f"Usuario {new_user} añadido correctamente")

        case "2":
            nueva_visita = input("A que usuario quieres añadir una visita? ").strip().title()
            
            for user in lista_usuarios:
                if user["nombre"] == nueva_visita:
                    user["visitas"] += 1
                    print(user)

        case "3":
            visita = input("De que usuario quieres ver las visitas? ").strip().title()
            for user in lista_usuarios:
                if user["nombre"] == visita:
                    if user["visitas"] == 1:
                        print(f"El usuario {user["nombre"]} ha visitado {user["visitas"]} vez")
                    else:
                        print(f"El usuario {user["nombre"]} ha visitado {user["visitas"]} veces")
        case "4":
            for user in lista_usuarios:
                if user["visitas"] == 1:
                    print(f"{user["nombre"]} ha visitado {user["visitas"]} vez")
                else:
                    print(f"{user["nombre"]} ha visitado {user["visitas"]} veces")
        case "x":
            print("Saliendo del programa")
            break
        case _ :
            print("Opción no reconocida. ")