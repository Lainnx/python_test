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

dict_reservas = {}
lista_clientes = []
reservas_maximas = 0

class Restaurante():
    def __init__(self,nombre,especialidad,turno,reservas_maximas):
        self.nombre=nombre
        self.especialidad=especialidad
        self.turno=turno
        self.reservas_maximas=reservas_maximas
        for i in self.turno:
            dict_reservas[i] = 0
        lista_clientes =[]
        # print(dict_reservas)
        

    def reserva(self,cliente,turno_r):
        if turno_r in dict_reservas:    #hay que coprobar antes de hacer el for y comparar con turno_r
            for i in self.turno:
                if i == turno_r:
                    if dict_reservas[i] < self.reservas_maximas:
                        dict_reservas[i] +=1
                        cliente.turno_reservado=turno_r
                        lista_clientes.append([cliente.nombre,cliente.turno_reservado])
                        print(f"Reserva realizada {cliente.nombre} turno {cliente.turno_reservado}. Reservas actuales:{dict_reservas[i]}")
                    else:
                        print(f"No se ha podido realizar la reserva(turno {turno_r}), pruebe en otro turno")
                        
        else:
            print(f"Este turno no existe: turno {turno_r}")
            

    def mostrar_reservas(self):
        print("*********************************")
        print(f"Nombre restaurante: {self.nombre}")
        # for i in range(len(lista_clientes)):
        #     for j in range(2):
        #         print(f"{lista_clientes[i][j]} i-{i} j-{j}")
        #         print(f"{lista_clientes[i]}")
        for i in range(len(lista_clientes)-1):
            for j in range(0,len(lista_clientes)-i-1):  #bubble sort(ni idea de como funciona xd)
                # print(i, len(lista_clientes))
                if lista_clientes[j][1] > lista_clientes[j+1][1]:
                    lista_clientes[j], lista_clientes[j+1] = lista_clientes[j+1],lista_clientes[j]
                    # print(i, lista_clientes)
        for cliente, turno in lista_clientes:
            print(f"{cliente} - {turno}")

class Cliente(Restaurante):
    def __init__(self,nombre):
        self.nombre=nombre
        turno_reservado = 0

    
    
    

cliente1 = Cliente("cliente1")
cliente2 = Cliente("cliente2")
cliente3 = Cliente("cliente3")
cliente4 = Cliente("cliente4")
cliente5 = Cliente("cliente5")
cliente6 = Cliente("cliente6")
cliente7 = Cliente("cliente7")
cliente8 = Cliente("cliente8")
cliente9 = Cliente("cliente9")
cliente10 = Cliente("cliente10")
cliente11= Cliente("cliente11")
cliente12= Cliente("cliente12")
restaurante1 = Restaurante("NombreR1","Especialidad1",(13,14,15,20,21,22),3)
restaurante2 = Restaurante("NombreR2","Especialidad2",(13,14,15,20,21,22),3)
restaurante1.reserva(cliente1,20)
restaurante1.reserva(cliente2,20)
restaurante1.reserva(cliente3,20)
restaurante1.reserva(cliente4,14)
restaurante1.reserva(cliente5,15)
restaurante1.reserva(cliente6,15)
restaurante1.reserva(cliente7,21)
restaurante1.reserva(cliente8,21)
restaurante1.reserva(cliente9,21)
restaurante1.reserva(cliente10,14)
restaurante1.reserva(cliente11,14)
restaurante1.reserva(cliente12,14)

# restaurante2.reserva(cliente1,14)
# restaurante2.reserva(cliente2,14)
# restaurante2.reserva(cliente3,14)
# restaurante2.reserva(cliente4,14)
# restaurante2.reserva(cliente5,15)
# restaurante2.reserva(cliente6,15)
# restaurante2.reserva(cliente7,16)
# restaurante2.reserva(cliente8,16)
# restaurante2.reserva(cliente9,16)
# restaurante2.reserva(cliente10,20)
# restaurante2.reserva(cliente11,20)
# restaurante2.reserva(cliente12,20)

print(dict_reservas)
# print(lista_clientes)

restaurante1.mostrar_reservas()
# restaurante2.mostrar_reservas()