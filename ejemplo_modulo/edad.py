def calcula_edad(fecha_nacimiento : str, fecha_actual : str) -> int:
    """
    Devolver la edad a partir de dos fechas

    Params
    fecha_nacimiento: str -> "dd/mm/aaaa"
    fecha_actual: str -> "dd/mm/aaaa"

    Return
    edad: int

    Códigos de error: 
    -1 : día o mes incorrecto
    -2 : la fecha de nacimiento debe ser igual o menor que la actual
    """
    def fecha_correcta(fecha):
        if int(fecha[0]) < 1 or int(fecha[0]) > 31:             #comprueba que el mes y el dia esten dentro de los rangos correctos
            return -1
        elif int(fecha[1]) < 1 or int(fecha[1]) > 12:
            return -1

    try:
        # fecha_nacimiento = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ").strip().split("/")
        fecha_nacimiento = fecha_nacimiento.strip().split("/")
        fecha_correcta(fecha_nacimiento)
        # fecha_actual = input("Introduce la fecha actual (DD/MM/AAAA): ").strip().split("/")
        fecha_actual = fecha_actual.strip().split("/")
        fecha_correcta(fecha_actual)
        

        edad = 0
        resta = []

        for i in range(3):
            resta.append(int(fecha_actual[i]) - int(fecha_nacimiento[i]))   #llena la lista resta[] con los valores de la resta

        if fecha_nacimiento[2] > fecha_actual[2]:
            return -2
        elif fecha_nacimiento[2] == fecha_actual[2] and fecha_nacimiento[1] > fecha_actual[1]:
            return -2
        elif fecha_nacimiento[2] == fecha_actual[2] and fecha_nacimiento[1] == fecha_actual[1] and fecha_nacimiento[0] > fecha_actual[0]:
            return -2
        else:
            if resta[2] > 0:    
                edad = int(resta[2])-1

            if resta[1] > 0 and resta[0] > 0: 
                edad += 1
            elif resta[1] == 0 and resta[0] == 0:
                print("Feliz cumpleaños!")
                edad += 1
        # print(resta)
        # print(f"fecha nacimiento: {fecha_nacimiento}\nfecha actual: {fecha_actual}\nedad: {edad}")

        return edad

    except ValueError:
        # print("Has introducido un valor incorrecto.")
        return -1
    
# fecha_nacimiento ="11/02/2000" #input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
# fecha_actual ="18/02/2025" #input("Introduce la fecha actual (DD/MM/AAAA): ")
# print(calcula_edad(fecha_nacimiento, fecha_actual))

def calcula_edad_2(fecha_nacimiento : str, fecha_actual : str) -> int:
    """ 
    Devolver la edad a partir de dos fechas

    Params
    fecha_nacimiento: str -> "dd/mm/aaaa"
    fecha_actual: str -> "dd/mm/aaaa"

    Return
    edad: int

    Códigos de error: 
    -1 : día o mes incorrecto
    -2 : la fecha de nacimiento debe ser igual o menor que la actual
    """
    fecha_actual = fecha_actual.split("/")
    dia_actual = int(fecha_actual[0])
    mes_actual = int(fecha_actual[1])
    any_actual = int(fecha_actual[2])

    fecha_nacimiento = fecha_nacimiento.split("/")
    dia_nacimiento = int(fecha_nacimiento[0])
    mes_nacimiento = int(fecha_nacimiento[1])
    any_nacimiento = int(fecha_nacimiento[2])

    #no puede ser que un mes sea menor a 1 mayor a 12
    #no puede ser que un dia sea menor a 1 y mayor que 31
    if(not 1 <= mes_actual <= 12) \
        or (not 1 <= mes_nacimiento <= 12) \
            or (not 1 <= dia_actual <= 31) \
                 or (not 1 <= dia_nacimiento <= 31): #not del caso correcto es el caso contrario, si esta fuera de este rango sera True
        return -1
    
    #No se puede calcular la edad si la fecha de nacimiento es posterior a la actual
    dif_anyos = any_actual - any_nacimiento
    dif_meses = mes_actual - mes_nacimiento
    dif_dias = dia_actual - dia_nacimiento
    # print(dif_anyos,dif_dias,dif_meses)
    if (dif_anyos < 0) or (dif_anyos == 0 and dif_meses < 0) or (dif_anyos == 0 and dif_meses == 0 and dif_dias < 0):
        return -2
    
    #calculo de la edad
    
    else:           #los años ya estan correctos, con el caso anterior hemos descartado años incorrectos, ahora estamos en el caso de los meses
        if (mes_nacimiento > mes_actual):   #si mes nacimiento mayor que mes actual aun no ha cumplido años 
            return dif_anyos-1
        elif (mes_actual == mes_nacimiento and dia_nacimiento > dia_actual):    #si el mes es el mismo y el dia nac es mayor(aun no ha cumplido años)
            return dif_anyos-1
        else:                   #todo lo demás ya ha cumplido años
            return dif_anyos
        
        

# fecha_nacimiento ="17/02/2000" #input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
# fecha_actual ="18/02/2025" #input("Introduce la fecha actual (DD/MM/AAAA): ")
# print(calcula_edad_2(fecha_nacimiento, fecha_actual))