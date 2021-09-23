from Elaboracion import Elaboracion

class ListaElab():
    def __init__(self):
        self.inicio = None #Nodo inicial de la lista
        self.fin = None

    def crearElaboracion(self, elaboracion):
        nuevo = Elaboracion(elaboracion) #Agregando data al nodo
        if self.inicio is None: #Verifica si el nodo tiene asignado un nodo inicial
            self.inicio = nuevo
        else: #Sino ya tiene asignado un nodo inicial llena otro nodo que no este en uso
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            self.fin = tmp.siguiente

    def estaVacia(self):
        return self.inicio == None

    def desencolar(self):
        try:
            tmp = self.inicio
            print("Se ensamblo la pieza "+str(tmp.elaboracion))
        except:
            pass

        if self.estaVacia():
            print("Cola vacía - Sin secuencia de trabajo")
        elif self.inicio == self.fin:
            self.inicio = self.fin = None
            print("Cola vacía - Sin secuencia de trabajo")
        else:
            self.inicio = self.inicio.siguiente
