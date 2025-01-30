"""
#Imprimeix una piramide
#############################
#rang = 5    #altura piramide
print("Escriu l'altura de la piramide :")
rangi = input()
rang = int(rangi)

print("De que vols que estigui feta la piràmide? Escriu un caracter :")
char = input()

#print("len" , len(char))
if len(char) == 1 :
    for x in range(rang):
        print(char * x)
    c=x+1
    for x in range(rang):
        print(char * c)
        #print(c)
        c=c-1
    else : 
        print("escriu nomes un caracter : ")
        char = input()
"""
"""
from datetime import datetime
print(datetime.now())

exponencial = 2 ** 3    #(2^3)
exponencial = 2 ** 0.5  #raiz cuadrada
division_entera = 20 // 6   #te da solo la parte entera
modulo = 20 % 3     #el resto de la division (el entero mas cercano 6*3=18 -->18-20= 2) so % 2 ==0 el numero es par

texto_formateado texto = f"{t1} {t2}" #vas vcambiando las variables y el formato a parte, es similar a C - https://ellibrodepython.com/cadenas-python#formateo-de-cadenas
texto final = "{} {}".format{t1, t2}

"""