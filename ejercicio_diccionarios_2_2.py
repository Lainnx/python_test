import os

#informacion de partida
tipo_entrada = {"estandar":9,"senior":6.9,"infantil":7.2}
#lo que el usuario va a comprar
lista_entradas_compradas = []

#iniciales que hay en el diccionario, que seran las opciones de compra
lista_iniciales = []
for clave in tipo_entrada:                  #llena la lista_iniciales con las iniciales de las claves del diccionario para poder usarlas de opciones
    lista_iniciales.append(clave[0])        #aunque el diccionario cambié lo unico que hay que tener en cuenta es que tienen que tener iniciales diferentes

compra_activa = True    #sistema de la bandera

while compra_activa:    
    menu = "Precios de las entradas:"
    for clave, valor in tipo_entrada.items():   #llama al diccionario y asigna la clave a clave y el valor a valor, si mas cosas en orden ","
        menu += f"\n{clave[0].upper()}. {clave.capitalize()} : {valor:.2f}€"   #clave[0] es el 1er caracter, será la opcion

    menu += "\n\nF. Finalizar compra"
    menu += "\nX. Salir sin comprar"
    menu += "\nElija el tipo de entrada"
    menu += "\nA continuacion podra elegir la cantidad: "

    eleccion_entrada = input(menu).lower().strip()

    if eleccion_entrada == "x":
        print("Aplicación finalizada.")
        compra_activa = False
    elif eleccion_entrada == "f":
        if lista_entradas_compradas:    #si hay algo es 1
            pass
            # compra_activa = False   #cuando termine de comprar, la ultima sentencia, porque ya ha comprado
        else:   #si esta vacía es 0
            print("Aún no ha comprado nada\n")
    elif eleccion_entrada in lista_iniciales:
        #buscar la entrada que corresponde a la eleccion del cliente
        for clave, valor in tipo_entrada.items():
            if eleccion_entrada == clave[0]:    #la primera letra de laq clave
                try:    #porque pasamos de string a int, tiene que ser int
                    cantidad = int(input("Indique cuantas entradas desea: "))
                except ValueError:
                    print("Debe indicar un numero entero")  
                    break   #este break afecta solo al bucle mas interior
                tipo = clave
                precio = valor
                subtotal = precio * cantidad

    else:
        os.system("cls")
        print("Opcion incorrecta.\n")