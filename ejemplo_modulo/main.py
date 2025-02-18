# import edad as ed     #importa todo lo que hay en edad.py -como ed(optativo, alias), sino esta en la misma carpeta hay que poner ruta absoluta donde está el fichero

# print(edad.calcula_edad_2("01/05/1682","18/02/2025"))
# print(ed.calcula_edad_2("01/05/1682","18/02/2025"))

from edad import calcula_edad_2 as ce    #para importar solo una cosa especifica, no el fichero entero

if __name__ == "__main__":                  #si el fichero que se esta ejecutando es el principal que esta ejecutando, el fichero que llama a los demás, a los auxiliares
    print(ce("01/05/1682","18/02/2025"))    #si haces import main en otro fichero, esto no se ejecutará en el otro fichero
    print(ce.__doc__)
