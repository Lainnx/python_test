#Match = SWITCH
#

mes = "Enero"

match mes:  #segun el valor que tenga mes haremos algo
    case "Enero":
        print("Iré a NY")
    case "Febrero":
        print("Iré a Paris")
    case "marzo" | "Abril" | "Mayo":                 #case puede absorver varios valores
        print("Iré a Egipto")                        #no hay default pero hay (case _ :), se ejecuta cuando no es ninguna de las otras, es como el else en if/else
    case _ :
        print("Nose donde iré")