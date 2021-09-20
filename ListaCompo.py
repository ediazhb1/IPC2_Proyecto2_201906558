from Compo import Compo
class ListaCompo():
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar(self,componente): #insertar
        nuevo = Compo(componente)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            self.fin = tmp.siguiente
            nuevo.anterior = tmp
            
