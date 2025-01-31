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
"""
mayoria_edad = 18                   #para hacer el codigo mas flexible

edad = input("escribe tu edad :")   #no int(input()) por si introducen otro tipo de caracter que no se pueda convertir a int
                                    #convertir a int() despues de comprovar que el input es correcto
print(edad.isdigit())
print(edad.isdecimal())
print(edad.isnumeric())
print(edad.isalpha())

if not edad.isdigit():  #comprobando que NO se ha introducido un numero entero, lo considero un ERROR, si no hay error el input es correcto i pasamos a chekar condiciones
    print("debes introducir un numero entero")
elif 0 <= int(edad) < mayoria_edad:
    #print("todavia no puedes votar, te faltan " + str(18-edad) + " años")
    print(f"todavia no puedes votar, te faltan {mayoria_edad-int(edad)} años")
elif 18 <= int(edad) < 120:
    #print("puedes votar de hace " + str(edad-18) + " años")
    print(f"puedes votar de hace {int(edad)-mayoria_edad} años")               #https://ellibrodepython.com/cadenas-python#formateo-de-cadenas
else:
    print("no me lo creo")
  
"""
#Pedir al usuario un numero
#pedir otro numero
#si no son numeros le diremosque no se puede hacer i break
#pedir que operacion matematica quiere hacer (7 posiblidades)
    #suma, resta, multi, division, exp, div_ent, modulo
#si no es ninguna de estas mostrar mensaje de error, si divide por 0 tambien
#al final debe aparecer: 
#1 3 suma
#1 + 3 = 4
"""
n1 = input("numero 1? ")
n2 = input("numero 2? ")
op = input("que operacion quieres hacer? operaciones disponibles:\nsuma\nresta\nmulti (multiplicacion)\ndivision\nexp (exponencial)\ndiv_ent (division entera)\nmodulo\n:")
#f=2.5
#print(f.isfloat())
if n1.isnumeric():                              #x.issomething() - son funciones, no olvidar ()
    n1=float(n1)                                #ASIGNAR LAS CONVERSIONES in() o str()
elif n1.count(".") == 1:                              #decimales
    n1s = n1.split(".")
    if n1s[0].isnumeric() and n1s[1].isnumeric():
        n1=float(n1)
elif n1.startswith("-"):
    n1 = float(n1)
if n2.isnumeric():
    n2=float(n2)
elif n2.count(".") == 1:
    n2s = n2.split(".")
    if n2s[0].isnumeric() and n2s[1].isnumeric():
        n2=float(n2)
elif n2.startswith("-"):
    n2 = float(n2)
#if n1.count("-") == 1:  
if n1.startswith("-"):                           #para negativos
    n1 = float(n1)
#if n2.count("-") == 1:                              

#if n1.isnumeric() and n2.isnumeric():          #x.issomething() - son funciones, no olvidar ()
#    n1=float(n1)                               #ASIGNAR LAS CONVERSIONES in() o str()
#    n2=float(n2)
if True:
    if op == "suma":                            #operaciones
        print(f"{n1} + {n2} = {n1+n2}")
    elif op == "resta":
        print(f"{n1} - {n2} = {n1-n2}")
    elif op == "multi":
        print(f"{n1} * {n2} = {n1*n2}")
    elif op == "division":
        if n2 == 0:
            print("no se puede dividir por 0")
        else:
            print(f"{n1} / {n2} = {n1/n2}")
    elif op == "exp":
        print(f"{n1} ^ {n2} = {n1**n2}")
    elif op == "div_ent":
        print(f"{n1} // {n2} = {n1//n2}")
    elif op == "modulo":
        print(f"{n1} % {n2} = {n1%n2}")
    else:
        print("ERROR: operacion no reconocida")
else:
    print("tienes que introducir numeros, no se puede operar con el input dado")

"""     
        #ponemos el float aqui i provocamos error cuando se introduce algo que no es un numero -->excepcion para gestionar el error
num1 = float(input("escribe el primer numero ."))
if num1.isalpha():                              #si el input es alfanumerico, en vez e filtrar si son numeros e intentar distinguir que tipo de numero es filtrar cuando no
    print("no se puede hacer")                  #son numeros.
else:                                           #si introducimos ???? el isalpha no lo atrapa --> excepciones
    print("se puede hacer")