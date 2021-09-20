from tkinter import *
from tkinter import ttk
from Archivo import Archivo
from Help import Help

class main():
    def __init__(self):      
        self.raiz =Tk()
        self.raiz.title("Brazo Ensamblador")
        self.raiz.resizable(0, 0)
        windowWidth = self.raiz.winfo_reqwidth()
        windowHeight = self.raiz.winfo_reqheight()
        positionRight = int(self.raiz.winfo_screenwidth()/3 - windowWidth/3)
        positionDown = int(self.raiz.winfo_screenheight()/3 - windowHeight/3)
        self.raiz.geometry(f'{885}x{521}+{int(positionRight)}+{int(positionDown)}')


        self.menubar = Menu(self.raiz)

        frame1 = Frame(self.raiz, bg="#BEB2A7",relief="groove", bd=3)
        frame1.place(rely=0.09, relx=0.22, height=375, width=650)
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["Name", "Type", "Base Stat Total"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")
        
        combobox = ttk.Combobox(self.raiz, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])

        combobox.place(rely=0.13, relx=0.03)

        newlabel = Label(self.raiz, text="Seleccionar un producto\npara ser ensamblado", fg="black",font = "Verdana 10 bold")
        newlabel.place(rely=0.04, relx=0.01)

        newlabel = Label(self.raiz, text="Tabla de Ensamblaje", fg="black",font = "Verdana 11 bold")
        newlabel.place(rely=0.02, relx=0.50)

        self.frames()

    def carga(self):
        Arch = Archivo()

    def help(self):
        Ayuda = Help()

    def frames(self):
        self.raiz.config(menu=self.menubar)

        filemenu = Menu(self.menubar,tearoff=0)
        editmenu = Menu(self.menubar,tearoff=0)
        helpmenu = Menu(self.menubar,tearoff=0)

        self.menubar.add_cascade(label="Archivo", menu=filemenu)
        self.menubar.add_cascade(label="Reportes", menu=editmenu)
        self.menubar.add_cascade(label="Ayuda", menu=helpmenu)

        filemenu.add_command(label="Cargar Archivo", command=self.carga)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.raiz.quit)

        helpmenu.add_command(label="Ayuda", command=self.help)



x = main()
x.raiz.mainloop()
