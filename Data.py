import xml.etree.ElementTree as ET
from ListaLineas import ListaLineas
from ListaNameProd import ListaNameProd
from ListaCompo import ListaCompo
import re

ListadoNameProd = ListaNameProd()
ListadoLineas = ListaLineas()
ListadoCompo = ListaCompo()
#Analisis del archivo de maquina
#Se utilizó ListaLineas para hacer una lista de listas de Las lineas de produccion y los Componentes
#Se utilizó ListaNameProd para hacer una lista de listas de los nombres de producto y la elaboración
class Data():
    def __init__(self): 
        self.CLine = 0

    def rutaxml(self,rxml):        
        tree = ET.parse(rxml)
        root = tree.getroot()
        
        no = 0
        compo = 0
        time = 0
        name = ""
        for elemento in root:
            for lineas in elemento.iter("CantidadLineasProduccion"):
                self.CLine = lineas.text.replace(" ","").replace("\n","")         

        for i in range(1,int(self.CLine)+1):
            ListadoLineas.crearLineas(str(i))

        for element in root:
            for listado in element.iter("ListadoLineasProduccion"):
                for linea in listado.iter("LineaProduccion"):
                    for numero in linea.iter("Numero"):
                        no = numero
                        #print("Numero: "+numero.text.replace(" ","").replace("\n",""))
                    for componente in linea.iter("CantidadComponentes"):
                        #print("Componente: "+componente.text.replace(" ","").replace("\n",""))
                        compo = componente.text.replace(" ","").replace("\n","")
                    for tiempo in linea.iter("TiempoEnsamblaje"):
                        time = tiempo
                        #print("Tiempo: "+tiempo.text.replace(" ","").replace("\n",""))
                    conexion = ListadoLineas.buscarLinea(no.text.replace(" ","").replace("\n",""))
                    for j in range(1,int(compo)+1):
                        #print(j)
                        conexion.lista_compo.insertar(j)
                    #print("---------")


        for element2 in root:
            for list in element2.iter("ListadoProductos"):
                for prods in list.iter("Producto"):
                    for nombre in prods.iter("nombre"):
                        name = nombre.text.replace("\n","").lstrip(" ").rstrip(" ")
                        ListadoNameProd.crearNameProd(name)

        ExRe = re.compile(r'L\d*pC\d*p')
        x = ""         
        for element3 in root:
            for list3 in element3.iter("ListadoProductos"):
                for prods3 in list3.iter("Producto"):
                    for nombre3 in prods3.iter("nombre"):
                        conections1 = ListadoNameProd.buscarNameProd(nombre3.text.replace("\n","").lstrip(" ").rstrip(" "))
                    for elabs3 in prods3.iter("elaboracion"):
                        elaboration3 = elabs3.text.replace("\n","").lstrip(" ").rstrip(" ")   
                        elab = ExRe.finditer(elaboration3)  
                        for j in elab:
                            x = str(j.group()) 
                            conections1.lista_elabos.crearElaboracion(x)
                                

    def lineasTabla(self):
        return ListadoLineas.mostrarLineas()


    def getData(self):
        lista = []
        agregar = []




        for i in range(1,int(self.CLine)+1):
            x = ListadoCompo.mostrarTitulos1(str(i))
            agregar.append(len(x))
            max_item = max(agregar, key=int)

            lista.append(x)
            print(max_item)
            

            for i in range(0,len(lista)):
                while len(lista[i]) != int(max_item):
                    lista[i].append("No hacer nada")

        
        return lista

    def simulacion(self,producto):
        #NOMBRE PRODUCTO
        #print(producto)
        #LINEAS DE PRODUCCION
        #ListadoLineas.mostrarLineas()
        #COMPONENTES
        #print("---------------")
        #for i in range(1,int(self.CLine)+1):
        #    a = ListadoLineas.buscarLinea(str(i))
        #    inicio = a.lista_compo.inicio
        #    while inicio is not None:
        #        print(inicio.componente)
        #        inicio = inicio.siguiente
        #print("---------------")
        #SECUENCIA DE TRABAJO
        #aa = ListadoNameProd.buscarNameProd(producto)
        #inicios = aa.lista_elabos.inicio
        #while inicios is not None:
        #    print(inicios.elaboracion)
        #    inicios = inicios.siguiente

        ###########################################################
                    #ALGORITMO PRINCIPAL DE SISTEMA
            
        ListadoCompo.llenarLineas(self.CLine)
                  
        simulacion = ListadoNameProd.buscarNameProd(producto)  
        inicios = simulacion.lista_elabos.inicio
        secuencia = simulacion.lista_elabos.sinSecuencia()
        ExRe1 = re.compile(r'L\d*')
        ExRe2 = re.compile(r'C\d*')

        while secuencia is False:
            ERLinea = ExRe1.finditer(inicios.elaboracion)
            ERCompo = ExRe2.finditer(inicios.elaboracion)
            for j in ERLinea:
                actualLinea = ListadoLineas.buscarLinea(j.group().replace("L",""))      

            for k in ERCompo:
                actualLinea.lista_compo.algoritmo(j.group().replace("L",""),k.group().replace("C",""),self.CLine) 

            simulacion.lista_elabos.desencolar()
            inicios = simulacion.lista_elabos.inicio
            secuencia = simulacion.lista_elabos.sinSecuencia()

        
        #DESENCOLAR
        #inicios2 = aa.lista_elabos.inicio
        #while inicios2 is not None:
        #    print(inicios2.elaboracion)
        #    inicios2 = inicios2.siguiente

        