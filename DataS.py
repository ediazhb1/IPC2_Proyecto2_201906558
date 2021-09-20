import xml.etree.ElementTree as ET
from ListaProductos import ListaProductos
ListadoProducto = ListaProductos()
#Analisis del archivo de Simulación
class DataS():
    def rutaxml(self,rxml):        
        tree = ET.parse(rxml)
        root = tree.getroot()
        
        nombre = ""
        prod = ""
        for elemento in root:
            for name in elemento.iter("Nombre"):
                nombre = name.text.replace(" ","").replace("\n","")

            for listaprod in elemento.iter("ListadoProductos"):
                for productos in listaprod.iter("Producto"):
                    prod = productos.text.replace(" ","").replace("\n","")
                    ListadoProducto.crearProducto(prod)

