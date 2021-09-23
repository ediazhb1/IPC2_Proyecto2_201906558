from ListaElab import ListaElab
class nameProd:#Clase Nodo
    def __init__(self,name):
        self.name = name
        self.lista_elabos = ListaElab()
        self.siguiente = None #Apuntador