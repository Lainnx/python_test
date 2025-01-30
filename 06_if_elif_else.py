#Coindicionales
"""
llueve = True

if llueve:
    print("Cojeré el paraguas")
else:
    print("Iré a pasear")

print("resto del codigo")
"""
"""
lunes = False   #los lunes como pizza
jueves = True   #los jueves como paella
                #el resto de dias bocadillo
if lunes:
    print("como pizza")
elif jueves:
    print("como paella")
else:
    print("como bocadillo")
"""
#Ejercicio:
#Preguntar la edad al usuario
# si tiene menos de 12 años - eres un niño/a
# si tiene menos de 18 - eres un/a adolescente
# si tiene menos de 30 - eres muy joven
# si tiene menos de 40 - eres joven, pero menos
# si tiene más - tu puedes con todo
"""
edad = int(input("escribe tu edad :"))
if edad < 0:
    print("has introducido un numero negativo")                            
elif 0 <= edad < 12:           
    print("eres un niño")
elif 12 <= edad < 18:               #(12 <= edad) no hace falta, una vez pasa de la condicion 1 (<12) ya se que tiene mas de 12
    print("eres un adolescente")    #no es necesario pero no esta mal para prevenir valores negativos
elif 18 <= edad < 30:               #(0-12)18)30)40)resto)
    print("eres joven")
elif 30 <= edad < 40:
    print("eres joven pero menos")
elif edad == 69:
    pass                            #no hace nada, se puede usar de placeholder sin que salga error si no se que tiene que hacer aún
else:
    print("tu puedes con todo")
"""

#preguntar edad,
#si tiene menos de 0 o mas de 120 -no me lo creo
#si tiene menos de 18 - aun no puedes votar, te faltan x años
#si tiene 18 o mas -puedes votar de hace x años

edad = int(input("escribe tu edad :"))

if 0 <= edad < 18:
    #print("todavia no puedes votar, te faltan " + str(18-edad) + " años")
    print(f"todavia no puedes votar, te faltan {18-edad} años")
elif 18 <= edad < 120:
    #print("puedes votar de hace " + str(edad-18) + " años")
    print(f"puedes votar de hace {edad-18} años")               #https://ellibrodepython.com/cadenas-python#formateo-de-cadenas
else:
    print("no me lo creo")
    