
# import os
# os.system("cls")
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

print(menu)
opcion_humano = input("Elije tu opcion: ").strip()  #entra string

if opcion_humano not in ["1","2","3"]:      #compara con string
    print("Juego finalizado. Hasta pronto!")  
else:
    opcion_maquina = str(random.randint(1,3))   #randint da un int, pasamos a string para poder comparar

    resultado_partida = f""" 
Has elegido {opciones_juego[int(opcion_humano)-1]}
la maquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
 """                                                                        #-1 porque los indices empiezan por 0
    print(resultado_partida)
    if opcion_humano == opcion_maquina: 
        print("Empate ¯\_(ツ)_/¯")
    elif (opcion_humano == "1" and opcion_maquina == "3") \
        or (opcion_humano == "2" and opcion_maquina == "1") \
            or (opcion_humano == "3" and opcion_maquina == "2"):
        print("Ganas! ༼ つ ◕_◕ ༽つ")
    else:
        print("Pierdes! (╯°□°）╯︵ ┻━┻")