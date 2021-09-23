from Lineas import Lineas
class ListaLineas():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista

    def crearLineas(self, numero):
        nuevo = Lineas(numero) #Agregando data al nodo
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarLineas(self):
        x =[]
        x.append("Tiempo")
        tmp = self.inicio
        while tmp is not None:
            #print(tmp.numero)
            x.append("Linea "+tmp.numero)
            tmp = tmp.siguiente
        return x

    def buscarLinea(self, numero):
        tmp = self.inicio
        while tmp is not None:
            if tmp.numero == numero:
                return tmp
            tmp = tmp.siguiente
        return None
