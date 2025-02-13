'''
EJERCICIO 20: CALCULAR EDAD
Haz un programa que pida al usuario su fecha de nacimiento y la fecha actual.
El programa debe mostrar la edad del usuario.
"Tienes XX años"

Nota: Hay que verificar año, mes y día para obtener la edad real.
No vale sólo el año.
Si alguien nació el 6/2/2000 y hoy es 7/2/2025 tiene 24 años
'''
def fecha_correcta(fecha):
    if int(fecha[0]) < 1 or int(fecha[0]) > 31:             #comprueba que el mes y el dia esten dentro de los rangos correctos
        print("Dia introducido no valido")
        exit()
    elif int(fecha[1]) < 1 or int(fecha[1]) > 12:
        print("Mes introducido no valido")
        exit()

try:
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ").strip().split("/")
    fecha_actual = input("Introduce la fecha actual (DD/MM/AAAA): ").strip().split("/")

    fecha_correcta(fecha_nacimiento)
    fecha_correcta(fecha_actual)

    edad = 0
    resta = []
    for i in range(3):
        resta.append(int(fecha_actual[i]) - int(fecha_nacimiento[i]))
    edad = int(resta[2])-1
    if resta[1] > 0 and resta[0] > 0: 
        edad += 1
    elif resta[1] == 0 and resta[0] == 0:
        print("Feliz cumpleaños!")
        edad += 1
    print(resta)
    print(f"{fecha_nacimiento}, {fecha_actual}, {edad}")


except ValueError:
    print("Has introducido un valor incorrecto.")
