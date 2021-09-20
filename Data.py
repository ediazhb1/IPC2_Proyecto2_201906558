import xml.etree.ElementTree as ET
from ListaLineas import ListaLineas

ListadoLineas = ListaLineas()
#Analisis del archivo de maquina
class Data():
    def rutaxml(self,rxml):        
        tree = ET.parse(rxml)
        root = tree.getroot()
        
        x = 0
        no = 0
        compo = 0
        time = 0

        for elemento in root:
            for lineas in elemento.iter("CantidadLineasProduccion"):
                x = lineas.text.replace(" ","").replace("\n","")         

        for i in range(1,int(x)+1):
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
                        conexion.lista_compo.insertar(j)
