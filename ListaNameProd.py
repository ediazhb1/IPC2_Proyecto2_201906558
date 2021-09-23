from nameProd import nameProd

class ListaNameProd():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista

    def crearNameProd(self, name):
        nuevo = nameProd(name) #Agregando data al nodo
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def buscarNameProd(self, name):
        tmp = self.inicio
        while tmp is not None:
            if tmp.name == name:
                return tmp
            tmp = tmp.siguiente
        return None

    def mostrarNameProd(self):
        tmp = self.inicio
        while tmp is not None:
            print("***Nombre Producto: "+ tmp.name)
            tmp = tmp.siguiente
