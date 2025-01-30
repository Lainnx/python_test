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

n1 = input("numero 1? ")
n2 = input("numero 2? ")
op = input("que operacion quieres hacer? operaciones disponibles:\nsuma\nresta\nmulti (multiplicacion)\ndivision\nexp (exponencial)\ndiv_ent (division entera)\nmodulo\n:")
#f=2.5
#print(f.isfloat())
if n1.isnumeric() and n2.isnumeric():           #x.issomething() - son funciones, no olvidar ()
    n1=float(n1)                                  #ASIGNAR LAS CONVERSIONES in() o str()
    n2=float(n2)
    if op == "suma":
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