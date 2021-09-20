from tkinter import *
from tkinter import filedialog
from Data import Data
from DataS import DataS

analisis = Data()
analisis2 = DataS()

class Archivo():
    def __init__(self,):
        self.root =Tk()
        self.root.title("Brazo Ensamblador")
        self.root.geometry("735x321")
        self.root.resizable(0, 0)

        self.newframe = Frame(self.root, bg="#FF7700",relief="groove", bd=3)    
        self.newlabel = Label(self.newframe, text="Cargar archivo de\n configuración de máquina", fg="black",width=22,font = "Verdana 10 bold")
        self.boton1 = Button(self.newframe,text="Seleccionar archivo",width=15,height=2, command= lambda: self.click_boton1())
        self.labelerr1 = Label(self.newframe, text="No seleccionó archivo", fg="red",width=22,font = "Verdana 8 bold")
        self.labelacep1 = Label(self.newframe, text="Archivo guardado", fg="green",width=22,font = "Verdana 8 bold")

        self.newframe2 = Frame(self.root, bg="#0059b3",relief="groove", bd=3)    
        self.newlabel2 = Label(self.newframe2, text="Cargar archivos de\n simulación", fg="black",width=36,font = "Verdana 10 bold")
        self.boton2 = Button(self.newframe2,text="Seleccionar archivo",width=15,height=2, command= lambda: self.click_boton2())
        self.labelerr2 = Label(self.newframe2, text="No seleccionó archivo", fg="red",width=22,font = "Verdana 8 bold")
        self.labelacep2 = Label(self.newframe2, text="Archivo guardado", fg="green",width=22,font = "Verdana 8 bold")

        self.botonback = Button(self.root,text="Regresar",font = "Verdana 12 bold", command= lambda: self.click_boton3())

        self.agregar()

    def click_boton3(self):      
        self.root.destroy()

    def click_boton1(self):
        archivo1 = filedialog.askopenfilename(title="Seleccione archivo de configuración", filetypes=(("Extensible Markup Language","*.xml"),("Todos los archivos","*.*")))
        
        if archivo1 is None:        
            self.labelacep1.pack_forget()
            self.labelerr1.pack(pady=4,padx=25)
        else:
            rutaxml = archivo1
            analisis.rutaxml(rutaxml)
            self.labelerr1.pack_forget()
            self.labelacep1.pack(pady=4,padx=25)

    def click_boton2(self):
        archivo2 = filedialog.askopenfilename(title="Seleccione archivo de simulación", filetypes=(("Extensible Markup Language","*.xml"),("Todos los archivos","*.*")))
        
        if archivo2 is None:
            self.labelacep2.pack_forget()
            self.labelerr2.pack(pady=4,padx=25)
        else:
            rutaxml2 = archivo2
            analisis2.rutaxml(rutaxml2)
            self.labelerr2.pack_forget()
            self.labelacep2.pack(pady=4,padx=25)

    def agregar(self):
        self.newframe.place(rely=0.20, relx=0.05, height=150, width=310)
        self.newlabel.pack(pady=1,padx=50)
        self.boton1.pack(pady=3,padx=100)

        self.newframe2.place(rely=0.20, relx=0.55, height=150, width=310)
        self.newlabel2.pack(pady=1,padx=50)
        self.boton2.pack(pady=3,padx=100)

        self.botonback.place(rely=0.75, relx=0.42, width=125,height=65)
