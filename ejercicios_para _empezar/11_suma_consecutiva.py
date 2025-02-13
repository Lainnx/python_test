'''
EJERCICIO 11: SUMA CONSECUTIVA
Haz un programa que pida al usuario un número comprendido entre 1 y 10
y muestre la suma de todos los números anteriores 
empezando por el 1 y acabando en el propio número del usuario.

Por ejemplo, si escribe 3, 
la operación debe ser 1 + 2 + 3 = 6
Si escribe 5,
la operación debe ser 1 + 2 + 3 + 4 + 5 = 15

'''
try:
    suma = 0
    a = int(input("Introduce un numero entre el 1 y el 10: "))
    if 1 < a < 10:
        for i in range (a+1):
            suma += i
            # print(suma)
        print(f"La suma consecutiva de {a} es: {suma}") 
    else:
        print("Introduce un numero del 1 al 10")
except ValueError:
    print("Tienes que introducir un numero entero: ")