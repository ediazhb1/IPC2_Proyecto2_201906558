from tkinter import PhotoImage, filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.constants import COMMAND, LEFT, RIGHT, VERTICAL, YES

from Data import Data
from DataS import DataS
from grafos import grafos

analisis = Data()
analisis2 = DataS()
grafica = grafos()

comboVals = ""
class main(tk.Tk):
    
    def __init__(self):
        self.root =tk.Tk()
        self.root.title("Brazo Ensamblador")
        self.root.geometry("835x321")
        self.root.resizable(0, 0)

        self.newframe = tk.Frame(self.root, bg="#FF7700",relief="groove", bd=3)    
        self.newlabel = tk.Label(self.newframe, text="Cargar archivo de\n configuración de máquina", fg="black",width=22,font = "Verdana 10 bold")
        self.boton1 = tk.Button(self.newframe,text="Seleccionar archivo",width=15,height=2, command= lambda: self.click_boton1())
        self.labelerr1 = tk.Label(self.newframe, text="No seleccionó archivo", fg="red",width=22,font = "Verdana 8 bold")
        self.labelacep1 = tk.Label(self.newframe, text="Archivo guardado", fg="green",width=22,font = "Verdana 8 bold")

        self.newframe2 = tk.Frame(self.root, bg="#0059b3",relief="groove", bd=3)    
        self.newlabel2 = tk.Label(self.newframe2, text="Cargar archivos de\n simulación", fg="black",width=36,font = "Verdana 10 bold")
        self.boton2 = tk.Button(self.newframe2,text="Seleccionar archivo",width=15,height=2, command= lambda: self.click_boton2())
        self.labelerr2 = tk.Label(self.newframe2, text="No seleccionó archivo", fg="red",width=22,font = "Verdana 8 bold")
        self.labelacep2 = tk.Label(self.newframe2, text="Archivo guardado", fg="green",width=22,font = "Verdana 8 bold")

        self.botonback = tk.Button(self.root,text="Regresar\npara cargar",font = "Verdana 12 bold", command= lambda: self.click_boton3())
        self.agregar()

    def click_boton3(self):
        updates = FirstPage()
        updates.combobox1.set("")
        comboVals = analisis2.getData()
        updates.combobox1['values'] = (comboVals)

        tablaVals = analisis.lineasTabla()
        agregart = []
        agregart.append(tablaVals)

        total_rows1 = len(agregart)
        total_columns1 = len(agregart[0])

        for i in range(total_rows1):
            for j in range(total_columns1):         
                self.d = ttk.Entry(updates.frame1, width=25, font=('Arial',10,'bold'))
                self.d.grid(row=0, column=j)
                self.d.insert("end", agregart[i][j])
        
        self.root.destroy()
        
    def agregar(self):
        self.newframe.place(rely=0.20, relx=0.05, height=150, width=310)
        self.newlabel.pack(pady=1,padx=50)
        self.boton1.pack(pady=3,padx=100)

        self.newframe2.place(rely=0.20, relx=0.55, height=150, width=310)
        self.newlabel2.pack(pady=1,padx=50)
        self.boton2.pack(pady=3,padx=100)

        self.botonback.place(rely=0.75, relx=0.42, width=150,height=65)
       

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
        
        try:
            if archivo2 is None:
                self.labelacep2.pack_forget()
                self.labelerr2.pack(pady=4,padx=25)
            else:
                rutaxml2 = archivo2
                analisis2.rutaxml(rutaxml2)
                self.labelerr2.pack_forget()
                self.labelacep2.pack(pady=4,padx=25)    
            
        except:
            print("No se pudo cargar el archivo de Simulación")

class FirstPage():
    def __init__(self):      
        self.raiz =tk.Tk()
        self.raiz.title("Brazo Ensamblador")
        self.raiz.resizable(0, 0)
        windowWidth = self.raiz.winfo_reqwidth()
        windowHeight = self.raiz.winfo_reqheight()
        positionRight = int(self.raiz.winfo_screenwidth()/3 - windowWidth/3)
        positionDown = int(self.raiz.winfo_screenheight()/3 - windowHeight/3)
        self.raiz.geometry(f'{985}x{621}+{int(positionRight)}+{int(positionDown)}')

        self.menubar = tk.Menu(self.raiz)
        self.newlabel1 = tk.Label(self.raiz, text="Seleccionar un producto\npara ser ensamblado", fg="black",font = "Verdana 10 bold")
        self.newlabel2 = tk.Label(self.raiz, text="Tabla de Ensamblaje", fg="black",font = "Verdana 11 bold")
        self.combobox1 = ttk.Combobox(self.raiz,values=["--Sin Cargar Archivo--"])
        self.button1 = tk.Button(self.raiz,text="Iniciar Simulación",width=15,height=2, command= lambda: self.click_boton1())


        self.frame1 = tk.Frame(self.raiz, bg="#BEB2A7",relief="groove", bd=3)
        self.frame1.place(rely=0.09, relx=0.22, height=475, width=750)       

        self.barra()
        self.agregarContenido()
    

    def click_boton1(self):
        if self.combobox1.get() == "":
            tk.messagebox.showinfo("Error","Seleccione un producto")
        elif self.combobox1.get() == "--Sin Cargar Archivo--":
            tk.messagebox.showinfo("Error","Carge el archivo de Simulación")
        else:
            analisis.simulacion(self.combobox1.get())

            tablaVals2 = analisis.getData()

            tiempo = []
            extra = []
            for a in range(1,len(tablaVals2[0])+1):
                tiempo.append(a)
            extra.append(tiempo)


            total_rows1 = len(extra)
            total_columns1 = len(extra[0])

            for i in range(total_rows1):
                for j in range(total_columns1):         
                    self.d = ttk.Entry(self.frame1, width=25, font=('Arial',10))
                    self.d.grid(row=j+1, column=i)
                    self.d.insert("end", extra[i][j])
                        
            total_rows = len(tablaVals2)
            total_columns = len(tablaVals2[0])

            for i in range(total_rows):
                for j in range(total_columns):         
                    self.e = ttk.Entry(self.frame1, width=25, font=('Arial',10))
                    self.e.grid(row=j+1, column=i+1)
                    self.e.insert("end", tablaVals2[i][j])
                     

    def agregarContenido(self):
        self.newlabel1.place(rely=0.04, relx=0.01)    
        self.newlabel2.place(rely=0.02, relx=0.50)
        self.combobox1.place(rely=0.13, relx=0.03)    
        self.button1.place(rely=0.20, relx=0.05)

    def carga(self):
        self.raiz.destroy()
        main()
                
    def help(self):
        Help()

    def reporte(self):
        Reporte()

    def barra(self):
        self.raiz.config(menu=self.menubar)

        filemenu = tk.Menu(self.menubar,tearoff=0)
        editmenu = tk.Menu(self.menubar,tearoff=0)
        helpmenu = tk.Menu(self.menubar,tearoff=0)

        self.menubar.add_cascade(label="Archivo", menu=filemenu)
        self.menubar.add_cascade(label="Reportes", menu=editmenu)
        self.menubar.add_cascade(label="Ayuda", menu=helpmenu)

        filemenu.add_command(label="Cargar Archivo", command=self.carga)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.raiz.quit)

        helpmenu.add_command(label="Ayuda", command=self.help)

        editmenu.add_command(label="Reportes", command=self.reporte)

class Reporte():
    def __init__(self):
        self.raiz =tk.Tk()
        self.raiz.geometry("835x700")
        self.raiz.resizable(0, 0)
        self.raiz.title("Reportes")
        self.raiz.eval('tk::PlaceWindow . center')

        self.newframe = tk.Frame(self.raiz, bg="#004DFF",relief="groove", bd=3)    
        self.newlabel1 = tk.Label(self.newframe, text="Reporte Graphviz", fg="black",width=30,font = "Verdana 12 bold")
        self.button1 = tk.Button(self.newframe,text="Generar Grafico",width=15,height=2, command= lambda: self.click_boton1())

        self.agregar()

            
    def agregar(self):
        self.newframe.place(rely=0.05, relx=0.05, height=175, width=400)
        self.newlabel1.pack(pady=5,padx=50) 
        self.button1.place(rely=0.25, relx=0.35)

class Help():
    def __init__(self):
        self.raiz =tk.Tk()
        self.raiz.geometry("435x400")
        self.raiz.resizable(0, 0)
        self.raiz.title("Ayuda")
        self.raiz.eval('tk::PlaceWindow . center')

        self.newframe = tk.Frame(self.raiz, bg="#004DFF",relief="groove", bd=3)    
        self.newlabel1 = tk.Label(self.newframe, text="Información del Estudiante", fg="black",width=30,font = "Verdana 12 bold")
        self.newlabel2 = tk.Label(self.newframe, text="Hecho por: Eddy Fernando Díaz Galindo", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel3 = tk.Label(self.newframe, text="Carnet: 201906558", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel4 = tk.Label(self.newframe, text="Curso: Introducción a la programación 2", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel5 = tk.Label(self.newframe, text="Ingenieria en Ciencias y Sistemas", fg="black",width=35,font = "Verdana 10 bold")
        self.newlabel6 = tk.Label(self.newframe, text="4to. Semestre, USAC", fg="black",width=35,font = "Verdana 10 bold")

        self.newframe2 = tk.Frame(self.raiz, bg="#004DFF",relief="groove", bd=3)    
        self.newlabel7 = tk.Label(self.newframe2, text="Acerca de la Aplicación", fg="black",width=30,font = "Verdana 12 bold")
        self.newlabel8 = tk.Label(self.newframe2,text="Simulación de brazo robótico\nque puede construir cualquier producto \nensamblando automáticamente los\ncomponentes (partes) que lo conforman.", fg="black",font = "Verdana 10",width=40)
        self.newlabel9 = tk.Label(self.newframe2,text="Se utiliza python y tipos de\ndatos abstractos para ejecutar este programa.", fg="black",font = "Verdana 10",width=40)
   
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

x = FirstPage()
x.raiz.mainloop()