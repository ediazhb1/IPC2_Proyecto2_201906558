from Productos import Productos
class ListaProductos():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista

    def crearProducto(self, producto):
        nuevo = Productos(producto) #Agregando data al nodo
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarProducto(self):
        tmp = self.inicio
        while tmp is not None:
            print("***Producto: "+ tmp.producto)
            tmp = tmp.siguiente