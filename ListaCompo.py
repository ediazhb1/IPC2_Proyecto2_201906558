from ListaContenido import ListaContenido
from typing import List
from Compo import Compo
from ListaTitulos import ListaTitulos
from ListaProductos import ListaProductos

ListadoTitulos = ListaTitulos()

class ListaCompo():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0
        self.posbrazo = None
        self.posbrazofin = None
        self.contador = 0
        self.lineaprincipal = []

    def insertar(self,componente): #insertar componente
        nuevo = Compo(componente)
        if self.inicio is None:
            self.inicio = nuevo
            self.posbrazo = self.inicio
            self.size +=1
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            self.fin = tmp.siguiente
            nuevo.anterior = tmp                  

    def llenarLineas(self,total):
        for i in range(1,int(total)+1):
            ListadoTitulos.crearTitulos(str(i))                  
            
    def algoritmo(self,lineaActual,compoMeta,totalineas):        
        tmp1 = self.inicio
        tmp2 = self.fin
       
        #print("Linea actual: ",lineaActual)
  
        if lineaActual not in self.lineaprincipal:
            #ListadoTitulos.crearTitulos(lineaActual)
            self.lineaprincipal.append(lineaActual+compoMeta)
            tmp3 = self.posbrazo
        else:
            tmp3 = self.posbrazofin

        conexion = ListadoTitulos.buscarTitulos(lineaActual)

        if int(tmp3.componente) < int(compoMeta):
            #print("PRIMER CASO - FLECHA BAJAR")
            #print("Posicion del brazo:",int(tmp3.componente),"Componente meta:",int(compoMeta))

            if self.contador == 0:
                tmp1 = tmp3
                self.contador +=1
            else:
                tmp1 = tmp3.siguiente

            while tmp1 is not None:
                conexion.lista_conte.crearContenido("Mover brazo – componente "+str(tmp1.componente))
                if int(tmp1.componente) == int(compoMeta):
                    self.posbrazo = tmp1
                    conexion.lista_conte.crearContenido("Ensamblar componente "+str(tmp1.componente))

                    for i in range(1,int(totalineas)+1):
                        if i == int(lineaActual):
                            i +=1
                            if i > int(totalineas):
                                break
                        
                        #print(i)
                        #conexion2 = ListadoTitulos.buscarTitulos(str(i))
                        #conexion2.lista_conte.crearContenido("No Hacer nada")
                        if i == int(totalineas):
                            break
                    #print("--------")
                        #conexion2 = ListadoTitulos.buscarTitulos(str(b))
                        #conexion2.lista_conte.crearContenido("No Hacer nada")
                                     
                    break
                tmp1 = tmp1.siguiente  

        elif int(tmp3.componente) > int(compoMeta):
            #print("SEGUNDO CASO - FLECHA SUBIR")
            #print("Posicion del brazo:",int(tmp3.componente),"Componente meta:",int(compoMeta))

            if self.contador == 0:
                tmp1 = tmp3
                self.contador +=1
            else:
                tmp1 = tmp3.siguiente

            while tmp2 is not None:
                conexion.lista_conte.crearContenido("Ensamblar componente "+str(tmp2.componente))
                if int(tmp2.componente) == int(compoMeta):
                    self.posbrazo = tmp2
                    conexion.lista_conte.crearContenido("Ensamblar componente "+str(tmp2.componente))
                    for i in range(1,int(totalineas)+1):
                        if i == int(lineaActual):
                            i +=1
                            if i > int(totalineas):
                                break
                        
                        #print(i)
                        if i == int(totalineas):
                            break
                    #print("--------")
                    break
                tmp2 = tmp2.anterior
        else:
            #print("TERCER CASO")
            #print("Posicion del brazo:",int(tmp3.componente),"Componente meta:",int(compoMeta))
            if self.contador == 0:
                tmp3 = tmp3
                self.contador +=1
            else:
                tmp3 = tmp3.siguiente
            conexion.lista_conte.crearContenido("Mover brazo – componente "+str(tmp3.componente))
            conexion.lista_conte.crearContenido("Ensamblar componente "+str(tmp3.componente))
            for i in range(1,int(totalineas)+1):
                if i == int(lineaActual):
                    i +=1
                    if i > int(totalineas):
                        break
                        
                #print(i)
                if i == int(totalineas):
                    break
            #print("--------")
            self.posbrazofin = tmp3
            



    def mostrarTitulos1(self,i):
        x =[]
        a = ListadoTitulos.buscarTitulos(str(i))
        inicio1 = a.lista_conte.inicio
        while inicio1 is not None:
            x.append(inicio1.contenido)
            inicio1 = inicio1.siguiente
        
        #mytuple = tuple(x)
        return x