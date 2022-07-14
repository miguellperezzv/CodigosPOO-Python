import tkinter  as tk 
from tkinter import Tk, RIGHT, BOTH, RAISED, TOP
from threading import Timer
import threading
from logica.ContadorOctal import ContadorOctal
from logica.ContadorBinario import ContadorBinario
from logica.ContadorDecimal import ContadorDecimal
from logica.ContadorHexadecimal import ContadorHexadecimal
import time




class FrameContador:

    contando = False
    contador = ContadorOctal(0)
    timer = Timer(None, None)
    opcion = 0
    output=None
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x200")
        self.master_frame = tk.Frame(root)
        #self.master_frame.pack(fill=tk.BOTH, expand=True)
        self.root.title("Contador")
        self.opcion = tk.IntVar()
        btnContar = tk.Button( text="Contar", command= self.iniciar).grid(column=1, row=3)
        btnParar = tk.Button( text="Parar", command= self.detener).grid(column=2, row=3)
        btnCerrar = tk.Button(text="Cerrar", command= self.cerrar).grid(column=3, row=3)
        btnReiniciar = tk.Button(text="Reiniciar", command= self.reiniciar).grid(column=4, row=3)
        self.output = tk.Text(root, height = 5, width = 25, bg = "light cyan")

       
        tk.Radiobutton(root, text="Binario", variable=self.opcion, value=1, command=self.elegirSistema).grid(column=1, row=0, sticky="W")
        tk.Radiobutton(root, text="Octal", variable=self.opcion, value=2, command=self.elegirSistema).grid(column=2, row=0, sticky="W")
        tk.Radiobutton(root, text="Decimal", variable=self.opcion, value=3, command=self.elegirSistema).grid(column=3, row=0, sticky="W")
        tk.Radiobutton(root, text="Hexadecimal", variable=self.opcion, value=4, command=self.elegirSistema).grid(column=4, row=0, sticky="W")

        self.output.grid(column=5, row=5)

        self.contando=True
        self.timer = Timer(1, self.contar)
        self.timer.start()

    def contar(self):
        
        #print(self.contando)
        if self.contando==True:
            self.contador.contar()
            self.output.delete(1.0,"end")
            self.output.insert(1.0, self.contador.mostrarConteo())
        else:
            None
            self.output.delete(1.0,"end")
            self.output.insert(1.0, self.contador.mostrarConteo())
        time.sleep(1)
        self.contar()
        #threading.Timer(1, self.contar()).start()
        
        
        
    
    def detener(self):
        self.contando=False

    def iniciar(self):
        self.contando=True
    
    def cerrar(self):
        #self.timer.cancel()
        self.root.destroy()

    def elegirSistema(self):
        if self.opcion.get() == 1:
            print("BINARIO")
            self.contador =  ContadorBinario(self.contador.valor)
        if self.opcion.get() == 2:
            self.contador =  ContadorOctal(self.contador.valor)
        if self.opcion.get() == 3 :
            self.contador =  ContadorDecimal(self.contador.valor)
        if self.opcion.get() == 4:
            self.contador =  ContadorHexadecimal(self.contador.valor)
    
    def reiniciar(self):
        self.contador.valor=0
        
