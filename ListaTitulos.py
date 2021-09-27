from Titulos import Titulos
class ListaTitulos():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista

    def crearTitulos(self, numero2):
        nuevo = Titulos(numero2) #Agregando data al nodo
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def buscarTitulos(self, numero):
        tmp = self.inicio
        while tmp is not None:
            if tmp.numero2 == numero:
                return tmp
            tmp = tmp.siguiente
        return None
    
    def mostrarTitulos(self):
        tmp = self.inicio
        while tmp is not None:
            print("***Linea Titulo: "+ tmp.numero2)
            tmp = tmp.siguiente