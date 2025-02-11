#Tuplas
#son como listas pero inmutables (no se pueden cambiar), al ser inmutables python las trabaja de forma mas eficiente

mi_tupla =(3)           #() puede usarse tambien para ordenar operaciones
print(type(mi_tupla))   #int
mi_tupla = (3,)         #incluso sin parentesis
print(type(mi_tupla))   #tupla
mi_tupla = 3,4,5
print(type(mi_tupla))

tupla = ("Anna")
print(tupla)    #Anna
print(tupla[0]) #A
# tupla[0] = "Marta"  #Error, una vez creada no se puede cambiar
tupla = ("Anna", "Pou", 20, "anna@gmail.com")
print(tupla)    #('Anna', 'Pou', 20, 'anna@gmail.com') ||()
print(tupla[0]) #Anna

#Para cambir datos en una tupla hay que pasar a lista primero
lista_temporal = list(tupla)
print(lista_temporal)       #['Anna', 'Pou', 20, 'anna@gmail.com'] || []
lista_temporal[0] = "Marta" #['Marta', 'Pou', 20, 'anna@gmail.com'] || []
print(lista_temporal)
tupla = tuple(lista_temporal)   #pasamos lista a tupla para dejarla inmutable de nuevo
print(tupla)                    #('Marta', 'Pou', 20, 'anna@gmail.com') || ()

print(tupla[1:3])   #('Pou', 20), igual que en las listas, utilizan los mismos sistemas porque las dos son elementos indexados(la unica diferencia es que las tuplas son inmutables)

for item in tupla:
    print(item)
