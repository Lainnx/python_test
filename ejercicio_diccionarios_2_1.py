
lista_precios = [{"tipo":"estandar","precio":9.00,"numero":0,"id":1},{"tipo":"+65","precio":6.90,"numero":0,"id":2},{"tipo":"infantil","precio":7.20,"numero":0,"id":3},{"tipo":"dia_espectador","precio":5.00,"numero":0,"id":4}] 
lista_numero = []

while True:

    for precio in lista_precios:
        print(f"{precio["id"]} - Entrada {precio["tipo"]}: {precio["precio"]}")
    print(f"{len(lista_precios)+1} - Para crear Factura")
    print(f"{len(lista_precios)+2} - Para salir del programa\n")
    try:
        opcion = int(input())
        if opcion == len(lista_precios)+1:
            print("Saliendo del programa")
            exit()
        else:
            for precio in lista_precios:
                if precio["id"] == opcion:
                    precio["numero"] += int(input(f"Cuantas entradas {precio["tipo"]} quieres?"))
                    if precio["tipo"] == "infantil":
                        for entrada in lista_precios:
                            if entrada["tipo"] and entrada["tipo"]!="infantil":
                                pass
        
    except ValueError:
        print("Tienes que introducir un numero entero")