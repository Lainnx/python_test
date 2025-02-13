'''
EJERCICIO 12: SUMA DEL USUARIO
En una sola instrucción (de una vez) pide al usuario
que introduzca varios números (fíjate en el ejemplo).
La respuesta del programa será la suma de todos ellos.
Puede escribir cualquier cantidad de números.

Por ejemplo, si escribe
2, 5, 3
La respuesta debe ser:
"El resultado de la suma es 10" 
'''
def suma(*argv):
    suma = 0
    # print(argv)
    for string in argv:      #argv = ('6,5,9,8,7',)  una tupla de strings, NO ES MUTABLE PERO ES ITERABLE
        for i in string:
            if i.isnumeric():
                a = float(i)
                suma += a
    return suma

a = input("Introduce cualquier cantidad de numeros, separados por comas: ")
print(f"El resultado e la suma es {suma(a)}")