import xml.etree.ElementTree as ET
from ListaLineas import ListaLineas
from ListaNameProd import ListaNameProd
import re

ListadoNameProd = ListaNameProd()
ListadoLineas = ListaLineas()
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


    def simulacion(self,producto):
        #NOMBRE PRODUCTO
        print(producto)
        #LINEAS DE PRODUCCION
        ListadoLineas.mostrarLineas()
        #COMPONENTES
        print("---------------")
        for i in range(1,int(self.CLine)+1):
            a = ListadoLineas.buscarLinea(str(i))
            inicio = a.lista_compo.inicio
            while inicio is not None:
                print(inicio.componente)
                inicio = inicio.siguiente
        print("---------------")
        #SECUENCIA DE TRABAJO
        aa = ListadoNameProd.buscarNameProd(producto)
        inicios = aa.lista_elabos.inicio
        while inicios is not None:
            print(inicios.elaboracion)
            inicios = inicios.siguiente

        ###########################################################

        