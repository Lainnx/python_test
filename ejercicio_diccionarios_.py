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
cont =0
existe = True
while True:
    print("Menu:")
    print("1. Añadir un usuario")
    print("2. Añadirs una visita al usuario indicado")
    print("3. Mostrar las visitas del usuario que se decida")
    print("4. Mostrar las visitas de todos los usuarios")
    print("X. Para salir del programa")
    print(lista_usuarios)
    opcion = input("").strip().lower()

    match opcion:
        case "1":
            new_user = input("Introduce el nombre del usuario que deseas añadir: ").strip().title()
            # usuario_nuevo = {"nombre":user,"visitas":0}
            if lista_usuarios:                                          #si no hay nada en la lista el for no tiene sobre qué iterar
                for dic in lista_usuarios:
                    if dic["nombre"] == new_user:
                        print("Ese usuario ya existe")
                        print("user: ",new_user) 
                    else:
                        usuario_nuevo = {"nombre":new_user,"visitas":0}
                        lista_usuarios.append(usuario_nuevo) 
                        # break    
            else:
                usuario_nuevo = {"nombre":new_user,"visitas":0}
                lista_usuarios.append(usuario_nuevo)           
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "x":
            print("Saliendo del programa")
            break
        case _ :
            print("Opción no reconocida. ")