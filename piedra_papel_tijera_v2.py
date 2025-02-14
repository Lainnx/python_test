
import os
os.system("cls")    #para limpiar pantalla
""" 
Lista de mejoras:

-Limitar un maxmimo de partidas
-Contar cuantas veces ha ganado, perdido y empatado
-Preguntar alias usuario

-Guardar los resultados
 """

import random

#lista de las opciones
opciones_juego = ["Piedra","Papel","Tijeras"]
opciones_juego = ["🥌","🧻","✂"]       #python acepta emojis

#Informar al usuario de las opciones del juego
menu = f""" 
PIEDRA - PAPEL - TIJERAS
------------------------

1. {opciones_juego[0]}
2. {opciones_juego[1]}
3. {opciones_juego[2]}

Escribe cuanquier otra cosa para salir.
"""
nombre_usuario = input("Introduce el nombre de usuario: ")
print("Buena suerte! ^^")

gana = 0
pierde = 0
empata = 0

while True:     #Para que pueda volver a intntar introducir el numero
    try:        #como hacemos conversion a int necesitamos el try en caso que el usuario introduzca un no numero
        numero_partidas = int(input("Cuantas partidas quieres jugar? (Entre 1 y 5, 0 para salir): "))   #entra string -> convierte a int
        if numero_partidas == 0:    #compara con 0 int porque pasamos a int arriba
            print(f"Hasta pronto ( ´･･)ﾉ({nombre_usuario})")
            # os.sistem("exit")  #sale del programa, con exit() da bucle infinito, al poner la condicion del while de abajo ya no hace falta,
            # nunca ejecutara el codigo del juego si numero_partidas = 0
            break
        elif 1 <= numero_partidas <= 5: #si numero de partidas entre 1 y 5 jugará, num partidas es un valor correcto
            break
        else:
            print("Has de introducir un número entre 1 y 5")
            
    except:
        print("Has de introducir un numero entero: ")   #en caso que no introduazca un numero correcto

contador_de_partidas = 1 #así nunca va a ser menor que 0 y no hay que comprar por debajo en el while siguiente

while contador_de_partidas <= numero_partidas:   # <=numero_partidas porque puede elegir 1 partida  || si numero partidas = 0 esto no se cumple nunca y nunca va a entrar ahí
    contador_de_partidas += 1   #ya esta en una partida, contador partidas +1, si quiere jugar 1 al entrar aqui contador partidas =2 y luego saldrá del bucle
        
#Informar al usuario de las opciones de juego
    print(menu)
    opcion_humano = input("Elije tu opcion: ").strip()  #entra string

    if opcion_humano not in ["1","2","3"]:      #compara con string
        print("Juego finalizado. Hasta pronto!") 
        break 
    else:
        opcion_maquina = str(random.randint(1,3))   #randint da un int, pasamos a string para poder comparar

        resultado_partida = f""" 
    Has elegido {opciones_juego[int(opcion_humano)-1]}
    la maquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
    """                                                                        #-1 porque los indices empiezan por 0
        print(resultado_partida)
        if opcion_humano == opcion_maquina: 
            print(f"~~ {nombre_usuario} ~~ Habéis empatado ¯\_(ツ)_/¯")
            empata += 1
        elif (opcion_humano == "1" and opcion_maquina == "3") \
            or (opcion_humano == "2" and opcion_maquina == "1") \
                or (opcion_humano == "3" and opcion_maquina == "2"):
            print(f"Enhorabuena! ++ {nombre_usuario} ++ Ganas! ༼ つ ◕_◕ ༽つ")
            gana += 1
        else:
            print(f"Mala suerte -- {nombre_usuario} -- Pierdes! (╯°□°）╯︵ ┻━┻")
            pierde += 1
    print(f""" 
        Has ganado {gana} veces
        Has perdido {pierde} veces
        Has empatado {empata} veces
        """)
print("Aplicación finalizada.")