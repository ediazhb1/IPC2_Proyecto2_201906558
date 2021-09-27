from Contenido import Contenido
class ListaContenido():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None
        self.size = 0

    def crearContenido(self, contenido):
        nuevo = Contenido(contenido) #Agregando data al nodo
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
            self.size +=1
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    

