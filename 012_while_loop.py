#WHILE LOOP (mientras se cumple una condicion el bucle se va a ejecutar)
"""
num = 5
while num >  0:
    print(num)
    num -= 1
else:                                    #funciona cuando no hay un break
    print("has entrado en el else")
"""
"""
num = 5
while True:
    print(num)
    num -= 1
    if num == 0:
        break
else:                                    #funciona cuando no hay un break
    print("has entrado en el else")
"""
monedas = 10

while True:
    prestamo = float(input("Cuantas monedas necesitas? "))
    if prestamo <= monedas:
        monedas -= prestamo
    else:
        print("No tengo suficientes monedas")
        break