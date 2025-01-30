"""
String - Cadenas de texto
"""

#Str1 = 'hola1'
#Str2 = "hola2"
#Str3 = """hola3"""

#print(Str1 + " " + Str2 + " " + Str3)
"""
#print("nombre?")
nombre = input("Nombre? ")
#print(type(nombre))
#print("apellido?")
apellido = input("Apellido? ")
#print(type(apellido))
#print("edad?")
edad = input("Edad? ")
edadint = int(edad)
#print(type(edadint))
datos="Me llamo " + nombre + " " + apellido + " y tengo " + edad + " años"
print(datos)
"""

frase = "esto es una frase un poco larga, pero podria serlo mas"
#Primer caracter del string
frase[0]
print("frase[0] - ", frase[0])

#Ultimo caracter del string | en python se puede contar hacia atras [-1] empieza por el final
print("frase[-1] - ", frase[-1])

#Los 6 primeros chars
print("frase[0:6] - ", frase[0:6])  # = frase[:6] |no poner nada y 0 es lo mismo
                                    # [inicio:fin]
#Los 6 últimos chars                                   |-1
print("frase[-6:] - ", frase[-6:])  #      |0|1|2|3|4|5|6    ||de -6 al final
                                    #      |m|a|n|z|a|n|a     |imaginar los numeros encima de las |, actuan como barreras y entre ellas cogemos las posiciones, al final no hay |
                                    #       [0:3] [3:6]
                                    #       man   zan
                                    #             [-4: ] #de -4 al final
                                    #             zana 
#Chars en posicion par
print("frase[::2] - ", frase[::2])  #de 2 en 2 |frase[::3] de 3 en 3
print("frase[::3] - ", frase[::3])  #
print("frase[::-1] - ", frase[::-1])#invierte la frase

#Cuantos chars hay en el string
print("len :", len(frase))

#Convertir el texto en mayusculas
print(frase.upper())
frase = frase.upper()
print(frase)

#Convertir a minusculas
print(frase.lower())
frase = frase.lower()
print(frase)

#Empezar el string por mayuscula
print(frase.capitalize())   #afecta solo al primer caracter, si no es una letra no lo hace (¿,¡...)
frase = frase.capitalize()

#Invertir mayuscular y minusculas
print(frase.swapcase())

#Contar caracteres | cuenta el numero de veces que estra chars en string
print("frase.count('Es')", frase.count("Es")) #frase.count('char') |char actua como un string, puedes poner mas de un char i contara en numero de veces que aparece

#Encontrar la posicion de un char o grupo de chars determinado
print("frase.find('a')", frase.find('a'))     #devuelve -1 si no existe el char o sequencia

#Verificar si un string si el texto empieza o acaba por cierto/s char/s | devuelve bool
frase1="https://google.com"
print("frase1.startswith('https') ", frase1.startswith('https'))

print("frase1.endswith('.com') ", frase1.endswith('.com'))

#Verificar si el texto (string) es convertible a numero
numero ="10"    #string
print(int(numero))  
print("numero.isnumeric() ",numero.isnumeric()) #solo numeros
print("numero.isalpha() ", numero.isalpha())    #solo texto
print("numero.isalnum() ", numero.isalnum())    #solo numeros y texto, sin caracteres especiales

#Cambiar caracteres
print("frase.replace('a', 'i') ", frase.replace("a", "i"))

#Contar el numero de palabras
palabras_en_frase = frase.split(" ")    #corta la frase por los espacios, se puede cortar por otros chars, el chars por el que se corta se pierde, en este caso los espacios
print("Lista de palabras ", palabras_en_frase) #crea una lista
print("len ",len(palabras_en_frase))    #numero de palabras
