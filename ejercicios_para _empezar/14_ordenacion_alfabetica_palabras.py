'''
EJERCICIO 14: ORDENACIÓN ALFABÉTICA DE PALABRAS
Haz un programa que pida al usuario un texto.
El programa debe ordenar las palabras del texto de forma alfabética.

Por ejemplo, si escribe: "hoy es domingo"
La respuesta debe ser: "domingo es hoy"
'''
texto = input("Introduce un texto: ").strip().split(" ")
texto = sorted(texto)
for i in texto:
    print(f"{i}", end = " ")