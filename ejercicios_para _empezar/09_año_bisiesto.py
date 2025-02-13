'''
EJERCICIO 9: AÑO BISIESTO
Haz un programa que pida al usuario un año y diga si es bisiesto o no
Averigua cual es el criterio
'''
try:
    y = int(input("Introduce un año: "))
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print(f"{y} es año bisiesto")
            else:
                print(f"{y} NO es año bisiesto")
        else:
            print(f"{y} es año bisiesto")
    else:
        print(f"{y} NO es año bisiesto")
except ValueError:
    print("tienes que introducir un numero")