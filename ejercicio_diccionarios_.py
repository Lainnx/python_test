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
import os

def print_users(lista_usuarios):
    print("Lista de usuarios: ")
    for name in lista_usuarios:
        print(name["nombre"])
    
lista_usuarios = []
lista_exist = []            #NO DECLARAR VARIABLES DENTRO DE BUCLES, QUE SE REINICIAN CADA ITERACION!

while True:
    print("Menu:")
    print("1. Añadir un usuario")
    print("2. Añadir una visita al usuario indicado")
    print("3. Mostrar las visitas del usuario que se decida")
    print("4. Mostrar las visitas de todos los usuarios")
    print("X. Para salir del programa")
    # print(lista_usuarios)
    # print(f"usuario {lista_usuarios} \nexist {lista_exist}")
    opcion = input("").strip().lower()                          #strip().lower() para quitar posibles espacios y x minuscula
    
    match opcion:
        case "1":
            new_user = input("Introduce el nombre del usuario que deseas añadir: ").strip().title()     #title pone la primera letra mayus y el resto en minus
            
            if new_user in lista_exist:                             #si new_user esta el la lista exist(en lista_usuarios hay un nombre igual)-> este usuario ya existe
                print("Este usuario ya existe: ", new_user)
            else:
                usuario_nuevo = {"nombre":new_user,"visitas":0}     #si new_user no esta en lista exist (||) se crea un nuevo usuario y se añade a lista_usuarios
                lista_usuarios.append(usuario_nuevo) 
                print(f"Usuario {new_user} añadido correctamente")
                lista_exist.append(usuario_nuevo["nombre"])         #se añaden los nombres que no estan ya, en la lista, si estamos añadiendo un usuario nuevo sabemos que no estará en 
                    # print(lista_usuarios, lista_exist)            #lista exist
                
        case "2":
            if lista_usuarios:                                      #si no hay usuarios no tiene sentido hacer ninguna operación, es condición imprescindible
                print_users(lista_usuarios)
                nueva_visita = input("A que usuario quieres añadir una visita? ").strip().title()
                # print(lista_exist)
                if nueva_visita in lista_exist:         #TÉCNICA DE FLAG, existe = False fuera del for, existe = True cuando encontramos usuario(dentro) i condicionales luego(mirar codigo profe)
                    for user in lista_usuarios:                 #PELIGROSO modificar lista_usuarios dentro del for                                      |con prints si el usuario existe o no
                        if user["nombre"] == nueva_visita:      #          modificar listas dentro de bucles cuando estas iterando con ellas
                            user["visitas"] += 1
                            break                               #cuando encontramos al usuario no vale la pena seguir iterando(los nombres son únicos)
                            print(user)
                else:
                    print("Este usuario NO existe: ", nueva_visita)
            else:
                print("No hay usuarios todavía.")
                
        case "3":
            if lista_usuarios:
                print_users(lista_usuarios)
                visita = input("De que usuario quieres ver las visitas? ").strip().title()

                if visita in lista_exist:
                    for user in lista_usuarios:
                        if user["nombre"] == visita:
                            if user["visitas"] == 1:
                                print(f"El usuario {user["nombre"]} ha visitado {user["visitas"]} vez")
                            else:
                                print(f"El usuario {user["nombre"]} ha visitado {user["visitas"]} veces")
                            break
                else:
                    print("Este usuario NO existe: ", visita)
            else:
                print("No hay usuarios todavía.")

        case "4":
            if lista_usuarios:
                for user in lista_usuarios:
                    if user["visitas"] == 1:
                        print(f"{user["nombre"]} ha visitado {user["visitas"]} vez")
                    else:
                        print(f"{user["nombre"]} ha visitado {user["visitas"]} veces")
            else:
                print("No hay usuarios todavía.")

        case "x":
            print("Saliendo del programa")
            break

        case _ :
            print("Opción no reconocida. ")

        #1, resolucion pocha, hay que declarar existe dentro del case(para que se reinicie en cada iteracion), mejor con lista_exist(que se puede usar en los otros case)
            # existe = 0
            # usuario_nuevo = {"nombre":user,"visitas":0}
            # if lista_usuarios:                                      #si no hay nada en la lista el for no tiene sobre qué iterar
                # for user in lista_usuarios:                         #user es un diccionario, iteramos sobre todos los de la LISTA DE USUARIOS
                #     if user["nombre"] not in lista_exist:           
                #         lista_exist.append(user["nombre"])          
                #         print("EXIST: ",lista_exist)
                #         print("user", user["nombre"])
                # if user["nombre"] == new_user:
                    #     existe += 1
                    #     print(existe) 
                # if existe == 0:
                #     usuario_nuevo = {"nombre":new_user,"visitas":0}
                #     lista_usuarios.append(usuario_nuevo) 
                #     print(f"Usuario {new_user} añadido correctamente")
                # else:
                #     print("Ese usuario ya existe")
                #     print("user: ",new_user)
                    # user["visitas"] += 1
            # else:                                                       #el primer elemento de la lista,
            #     usuario_nuevo = {"nombre":new_user,"visitas":0}
            #     lista_usuarios.append(usuario_nuevo)
            #     print(f"Usuario {new_user} añadido correctamente")
            #     lista_exist.append(usuario_nuevo["nombre"])             #para añadir el primer nombre a la lista, sino la lista va con 1 de retraso
