'''
EJERCICIO 17: SEGUNDO NÚMERO MAYOR
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el segundo número mayor.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
"El segundo número mayor es 6"
'''
try:
    numeros = sorted(input("Introduce una serie de numeros entre el 1 y el 20 separados por comas: ").strip().split(","))
    flag = False
    Smayortemp = 0
    for n in numeros:
        if float(n) < 1 or float(n) > 20:
            print("Introduce numeros entre el 1 y el 20")
            exit()
    for i in range(len(numeros)):
        if numeros[-i] == numeros[-i-1]:        
            Smayor = numeros[-i-2]
            if int(Smayor) > Smayortemp:
                Smayortemp = int(Smayor)
            else:
                print(f"El segundo mayor es print 1 {Smayor}")
                flag = True
                break
        else:
            continue #coge el 2o empezando por detras, como esta ordenado de menor a mayor este sera el segundo mayor
    if not flag:
        print(f"El segundo mayor es print 1 {numeros[-2]}")
    
            
except ValueError:
    print("tienes que introducir numeros ")
except IndexError:
    print(f"El segundo mayor es print 1 {numeros[-2]}")