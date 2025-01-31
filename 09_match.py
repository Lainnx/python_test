#Match = SWITCH
#
"""
mes = "Enero"

match mes:  #segun el valor que tenga mes haremos algo
    case "Enero":
        print("Iré a NY")
    case "Febrero":
        print("Iré a Paris")
    case "Marzo" | "Abril" | "Mayo":                 #case puede absorver varios valores
        print("Iré a Egipto")                        #no hay default pero hay (case _ :), se ejecuta cuando no es ninguna de las otras, es como el else en if/else
    case _ :
        print("Nose donde iré")
"""
"""
import os
os.system("cls")

try:                                    #Porque se puede roducir una excepcion a causa del input del usuario
    n1 = float(input("numero 1? "))     #con float() aqui forzamos error si no se introducen numeros y lidiamos con ellos con los except
    n2 = float(input("numero 2? "))     #
    op = input("que operacion quieres hacer? operaciones disponibles:\nsuma\nresta\nmulti (multiplicacion)\ndivision\nexp (exponencial)\ndiv_ent (division entera)\nmodulo\n:")
    
    match op:
        case "suma":                            #operaciones
            print(f"{n1} + {n2} = {n1+n2}")
        case "resta":
            print(f"{n1} - {n2} = {n1-n2}")
        case "multi":
            print(f"{n1} * {n2} = {n1*n2}")
        case "division":
            print(f"{n1} / {n2} = {n1/n2}")
        case "exp":
            print(f"{n1} ^ {n2} = {n1**n2}")
        case "div_ent":
            print(f"{n1} // {n2} = {n1//n2}")   #aqui falta para no dividir por 0
        case "modulo":
            print(f"{n1} % {n2} = {n1%n2}")     #aqui falta para no dividir por 0........ con excepciones te ahorras 3 if/else 
        case _ :
            print("ERROR: operacion no reconocida")
except ValueError:                                  #si se pone un try hay que poner al menos un except
    print("tienes que introducir un numero valido en cifras")
except ZeroDivisionError:
    print("no se puede dividir por 0")
"""

#Ejercicio: 
#Preguntar al ususario que dia de la semana es (lunes, martes...)
#lunes: "Toca sistemas"
#Martes, miercoles, jueves o viernes: "Toca python"
#Sabado, Domingo: "Es fin de semana"
#Otra cosa: "Creo que estas confundido"

"""
dia = input("que dia es? ")
dia = dia.lower()                           #porque los case son todos en minuscula, por si el usuario introduce alguna mayuscula
match dia:
    case "lunes" :
        print("toca sistemas")
    case "martes"|"miercoles"|"jueves"|"viernes" :
        print("toca python")
    case "sabado"|"domingo":
        print("toca descansar")
    case _ :
        print("creo que estas confundido")
"""