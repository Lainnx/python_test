'''
EJERCICIO 15: LETRAS DE UN TEXTO
Haz un programa que pida al usuario un texto.
El programa debe mostrar las letras que aparecen en ese texto
ordenadas de forma alfabética, pero solo una vez por cada letra,
y siempre en minúsculas.

Por ejemplo, si escribe: "Hoy es domingo"
La respuesta debe ser: "deghimny"
'''
texto = input("Escribe un texto: ").strip().lower().split(" ")
texto = "".join(texto)
lista_e = []
for letra in texto:
    if letra in lista_e:
        pass
    else:
        lista_e.append(letra)
lista_e = sorted("".join(lista_e))
for letra in lista_e:
    print(f"{letra}",end="")