from ListaCompo import ListaCompo
class Lineas:#Clase Nodo
    def __init__(self,numero):
        self.numero = numero
        self.lista_compo = ListaCompo()
        self.siguiente = None #Apuntador