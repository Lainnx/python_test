#EXCEPCIONES
#Son errores que se producen durante la ejecucion del programa y lo interrumpen

import os
os.system("cls")        #para limpiar pantalla en windows



"""

try:            #lo que intenta hacer
    print(1/0)                                 #operacion imposible para python
    print("despues de la division por 0")   #no se ejecuta, cuando encuentra el fallo salta al except
except:         #lo que se va a ejecutar cuando se produce el error
    print("nose puede dividir por 0")   #en vez de parar el programa se ejecuta la excepcion y continua ejecutando el programa

print("el prgrama continua... ")
"""                                     #capturamos posibles errores criticos y los gestionamos para que tengan una salida digna
#try /except -- si hay try debe haber except,  el try dice al programa que esté atento a posibles errores
try:
    num = float(input("un numero? "))
except ValueError:                              #error de conversion de tipos
    print("has de introducir un numero en cifras")
except ZeroDivisionError:                       #error por division por 0
    print("no se puede dividir por 0")
except:                                         #error genérico
    print("ha ocurrido un error")
else:                                               #optativo
    print("else: esto se ejecuta si no se levanta la excepcion")
finally:                                            #optativo       #mas info en 06_if_elif_else.py
    print("finally: este se ejecuta siempre")
print("el programa continua")