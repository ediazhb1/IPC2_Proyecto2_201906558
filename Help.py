from tkinter import *
from tkinter import filedialog

class Help():
    def __init__(self):
        self.raiz =Tk()
        self.raiz.geometry("435x400")
        self.raiz.resizable(0, 0)
        self.raiz.title("Ayuda")
        self.raiz.eval('tk::PlaceWindow . center')

        self.newframe = Frame(self.raiz, bg="#004DFF",relief="groove", bd=3)    
        self.newlabel1 = Label(self.newframe, text="Información del Estudiante", fg="black",width=30,font = "Verdana 12 bold")
        self.newlabel2 = Label(self.newframe, text="Hecho por: Eddy Fernando Díaz Galindo", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel3 = Label(self.newframe, text="Carnet: 201906558", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel4 = Label(self.newframe, text="Curso: Introducción a la programación 2", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel5 = Label(self.newframe, text="Ingenieria en Ciencias y Sistemas", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel6 = Label(self.newframe, text="4to. Semestre, USAC", fg="black",width=35,font = "Verdana 10 bold")

        self.newframe2 = Frame(self.raiz, bg="#004DFF",relief="groove", bd=3)    
        self.newlabel7 = Label(self.newframe2, text="Acerca de la Aplicación", fg="black",width=30,font = "Verdana 12 bold")
        self.newlabel8 = Label(self.newframe2,text="Simulación de brazo robótico\nque puede construir cualquier producto \nensamblando automáticamente los\ncomponentes (partes) que lo conforman.", fg="black",font = "Verdana 10",justify= CENTER,width=40)
        self.newlabel9 = Label(self.newframe2,text="Se utiliza python y tipos de\ndatos abstractos para ejecutar este programa.", fg="black",font = "Verdana 10",justify= CENTER,width=40)
   
        self.agregar()

    
    def agregar(self):
        self.newframe.place(rely=0.05, relx=0.05, height=175, width=400)
        self.newlabel1.pack(pady=5,padx=50)
        self.newlabel2.pack(pady=0,padx=50)
        self.newlabel3.pack(pady=0,padx=50)
        self.newlabel4.pack(pady=0,padx=50)
        self.newlabel5.pack(pady=0,padx=50)
        self.newlabel6.pack(pady=0,padx=50)

        self.newframe2.place(rely=0.50, relx=0.05, height=175, width=400)
        self.newlabel7.pack(pady=5,padx=50)
        self.newlabel8.pack(pady=0,padx=15)
        self.newlabel9.pack(pady=0,padx=15)