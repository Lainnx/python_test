""" 
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 
En cualquier momento hay que poder finalizar el proceso
sin que se produzca la compra
 """

num_est = 0
num_65 = 0
num_infantil = 0
total = 0

lista_precios = [{"tipo":"estandar","precio":9.00,"numero":0},{"tipo":"+65","precio":6.90,"numero":0},{"tipo":"infantil","precio":7.20,"numero":0}] #NO DECLARAR DENTRO DE BUCLES!"!!!!!!"

while True:
    
    try:
        op = input("""Que tipo de entrada quieres comprar:
        1- Entrada estándar: 9.00
        2- Mayores de 65 años (seniors) : 6.90
        3- Infantiles : 7.20
        4- Factura
        5- Salir del programa\n""").strip().lower()
        # print(lista_precios)
        match(op):
            case "1":
                num_est = int(input("Cuantas entradas estandar quieres comprar? ").strip())
                # print(num_est)
                for precio in lista_precios:
                    if precio["tipo"] == "estandar":
                        precio["numero"] += num_est
                        # print(precio)
                        break
            case "2":
                num_65 = int(input("Cuantas entradas senior quieres comprar? ").strip())
                for precio in lista_precios:
                    if precio["tipo"] == "+65":
                        precio["numero"] += num_65
                        # print(precio)
                        break
            case "3":
                if num_est or num_65:
                    num_infantil = int(input("Cuantas entradas infantiles quieres comprar? ").strip())
                    for precio in lista_precios:
                        if precio["tipo"] == "infantil":
                            precio["numero"] += num_infantil
                            # print(precio)
                            break
                else:
                    print("Debes ir acompañado de un adulto")
            case "4":
                for entrada in lista_precios:
                    print(f"{entrada["tipo"]}: {entrada["precio"]} € x {entrada["numero"]} = {(entrada["precio"] * entrada["numero"]):.2f}")    #:.2f para mostrar solo 2 decimales
                    total = total + (entrada["numero"]*entrada["precio"])
                print(f"El total es: {total:.2f}")
                break
                    
            case "5":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion no reconocida.")
    except ValueError:
        print("Tienes que introducir un numero entero")
