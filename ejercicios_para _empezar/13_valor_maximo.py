'''
EJERCICIO 13: VALOR MÁXIMO
En una sola instrucción (de una vez) pide al usuario
que introduzca varios números.
La respuesta del programa será el valor máximo de todos ellos

Por ejemplo, si escribe
2, 5, 3
La respuesta debe ser:
"El valor máximo es 5" 
'''

maxim = 0
a = input("Introduce varios numeros separados por comas: ")
# for num in a:
#     if num.isnumeric():
#         if float(num) > maxim:
#             maxim = float(num)
print(f"el valor maximo es: {max(a)}")  #a es una string, si es iterable se puede usar el max