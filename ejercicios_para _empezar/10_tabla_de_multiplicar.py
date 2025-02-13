'''
EJERCICIO 10: TABLA DE MULTIPLICAR
Haz un programa que pida al usuario un número 
y muestre la tabla de multiplicar de ese número
desde 1 hasta 10, ambos incluidos
'''
try:
    a = int(input("Introduce un numero: "))
    for i in range(10+1):
        print(f"{a} x {i} = {a*i}")
except ValueError:
    print("tienes que introucir un numero entero")