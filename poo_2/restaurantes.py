""" 
Vamos a genstionar restaurantes #mas de uno,plural, objetos

Cada uno tiene:
-mombre
-especialidad
-turnos (puede haber como maximo 3 clientes)
        (si se realiza la reserva diremos "reserva realizada [nombre cliente]")
        (y si no "No se ha podido realizar la reserva, pruebe en otro turno)
-clientes

Del cliente vamos a necesitar (de momento)
sólo el nombre

Ejemplo de uso:
cliente1 = Cliente("Anna")
restaurante1 = Restaurante("NombreR1","Especialidad1",(13,14,15,20,21,22))
 """
import os
os.system("cls")

# class Restaurante():

#     def __init__(self,nombre,especialidad,turno,reservas_maximas=3,dict_reservas={},lista_clientes=[]):     #metodo de instancia, tiene que ver con la creacion del objeto
#         self.nombre=nombre
#         self.especialidad=especialidad
#         self.turno=turno
#         self.reservas_maximas=reservas_maximas
#         self.lista_clientes=lista_clientes
#         self.dict_reservas=dict_reservas
#         for i in self.turno:
#             self.dict_reservas[i] = 0
#         # print(dict_reservas)
        

#     def reserva(self,cliente,turno_r):
#         if turno_r in self.dict_reservas:    #hay que coprobar antes de hacer el for y comparar con turno_r
#             for i in self.turno:
#                 if i == turno_r:
#                     if self.dict_reservas[i] < self.reservas_maximas:
#                         self.dict_reservas[i] +=1
#                         cliente.turno_reservado=turno_r
#                         self.lista_clientes.append([cliente.nombre,cliente.turno_reservado]) #lista de listas
#                         print(f"Reserva realizada {cliente.nombre} turno {cliente.turno_reservado}. Reservas actuales:{self.dict_reservas[i]}")
#                     else:
#                         print(f"No se ha podido realizar la reserva(turno {turno_r}), pruebe en otro turno")
                        
#         else:
#             print(f"Este turno no existe: turno {turno_r}")
            

#     def mostrar_reservas(self):
#         print("*********************************")
#         print(f"Nombre restaurante: {self.nombre}")
#         # for i in range(len(lista_clientes)):
#         #     for j in range(2):
#         #         print(f"{lista_clientes[i][j]} i-{i} j-{j}")
#         #         print(f"{lista_clientes[i]}")
#         for i in range(len(self.lista_clientes)):
#             for j in range(0,len(self.lista_clientes)-i-1):  #bubble sort(ni idea de como funciona xd)
#                 # print(i, len(lista_clientes))
#                 if self.lista_clientes[j][1] > self.lista_clientes[j+1][1]:
#                     self.lista_clientes[j], self.lista_clientes[j+1] = self.lista_clientes[j+1],self.lista_clientes[j]
#                     # print(i, lista_clientes)
#         for cliente, turno in self.lista_clientes:
#             print(f"{cliente} - {turno}")

# class Cliente():
#     def __init__(self,nombre,turno_reservado=0):
#         self.nombre=nombre
#         self.turno_reservado=turno_reservado

    
    
    

# cliente1 = Cliente("cliente1")
# cliente2 = Cliente("cliente2")
# cliente3 = Cliente("cliente3")
# cliente4 = Cliente("cliente4")
# cliente5 = Cliente("cliente5")
# cliente6 = Cliente("cliente6")
# cliente7 = Cliente("cliente7")
# cliente8 = Cliente("cliente8")
# cliente9 = Cliente("cliente9")
# cliente10 = Cliente("cliente10")
# cliente11= Cliente("cliente11")
# cliente12= Cliente("cliente12")

# restaurante1 = Restaurante("NombreR1","Especialidad1",(13,14,15,20,21,22))
# restaurante2 = Restaurante("NombreR2","Especialidad2",(13,14,15,20,21,22))

# restaurante1.reserva(cliente1,20)
# restaurante1.reserva(cliente2,20)
# restaurante1.reserva(cliente3,20)
# restaurante1.reserva(cliente4,14)
# restaurante1.reserva(cliente5,15)
# restaurante1.reserva(cliente6,15)
# restaurante1.reserva(cliente7,21)
# restaurante1.reserva(cliente8,21)
# restaurante1.reserva(cliente9,21)
# restaurante1.reserva(cliente10,22)
# restaurante1.reserva(cliente11,22)
# restaurante1.reserva(cliente12,22)

# restaurante2.reserva(cliente1,13)
# restaurante2.reserva(cliente2,13)
# restaurante2.reserva(cliente3,15)
# restaurante2.reserva(cliente4,14)
# restaurante2.reserva(cliente5,15)
# restaurante2.reserva(cliente6,15)
# restaurante2.reserva(cliente7,14)
# restaurante2.reserva(cliente8,14)
# restaurante2.reserva(cliente9,16)
# restaurante2.reserva(cliente10,13)
# restaurante2.reserva(cliente11,20)
# restaurante2.reserva(cliente12,20)

# print(restaurante1.dict_reservas)
# # print(lista_clientes)
# print(restaurante2.dict_reservas)
# # restaurante1.mostrar_reservas()
# # restaurante2.mostrar_reservas()
#####################################################################################
#solucion profe

class Cliente():
    def __init__(self,nombre):                                              #abstraccion, polimorfismo, 
        self.nombre=nombre

anna = Cliente("Anna")

class Restaurante():
    """ Informacion del Restaurante (cuando pasas el cursos por encima) """
    def __init__(self,nombre:str,especialidad:str,turnos:list):     #hay metodos para listas que no pueden aplicarse a las tuplas(poner o quitar elementos)
        self.nombre=nombre
        self.especialidad=especialidad
        self.turnos=turnos
        #atributo añadido para controlar los turnos
        self.reservas = {}  #diccionario de reservas, empieza vacío |si le pongo el self se podra obtener mas facilmente en todas partes
        for turno in turnos:   #en self.turnos se puede quitar el self porque turnos esta a la vista, el self es para acceder fuera de los metodos
            self.reservas[turno] = 0    #inicia el diccionario clave turno a 0 reservas

    def reservar(self,cliente,hora_reserva):
        #comprovar si la hora solicitada esta en los turnos disponibles
        if hora_reserva not in self.turnos:     #self.turnos porque var turnos no a la vista, self para info de objeto ||tambien podria ser self.reservas.keys()
            lista_turnos = [str(turno) for turno in self.turnos]  #itera en self.turnos y asigna a una lista pasando a str para poder imprimir con el .join
            mensaje = f"Lo sentimos no es posible la reserva a las: {hora_reserva}.\n"
            mensaje += f"Nuestros horarios disponibles: " + ", ".join(lista_turnos) + " horas."#separados por ", "turnos son int, habria que hacer una lista donde se convierten los numeros a str
            return mensaje
        else:
            pass
            

napoli = Restaurante("Napoli","Italiana",(12,13,14,15,20,21,22))

print(napoli.__doc__)   #el comentario de la clase
print(napoli.__dict__)  #en forma de diccionario, el contenido que tiene el objeto ahora
print(napoli.reservar(anna,4))