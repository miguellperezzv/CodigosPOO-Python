import tkinter  as tk 
from tkinter import Tk, RIGHT, BOTH, RAISED, TOP
from threading import Timer
import threading
from logica.ContadorOctal import ContadorOctal
import time




class FrameContador:

    contando = False
    contador = ContadorOctal()
    timer = Timer(None, None)
    opcion=""
    
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x200")
        self.master_frame = tk.Frame(root)
        self.master_frame.pack(fill=tk.BOTH, expand=True)
        self.root.title("Contador")
        btnContar = tk.Button(self.master_frame, text="Contar", command= self.iniciar)
        btnParar = tk.Button(self.master_frame, text="Parar", command= self.detener)
        btnCerrar = tk.Button(self.master_frame, text="Cerrar", command= self.cerrar)
        output = tk.Text(root, height = 5, width = 25, bg = "light cyan")

       
        tk.Radiobutton(root, text="Binario", variable=self.opcion, value=1, command=self.elegirSistema).pack()
        tk.Radiobutton(root, text="Octal", variable=self.opcion, value=2, command=self.elegirSistema).pack()
        tk.Radiobutton(root, text="Decimal", variable=self.opcion, value=3, command=self.elegirSistema).pack()
        tk.Radiobutton(root, text="Hexadecimal", variable=self.opcion, value=4, command=self.elegirSistema).pack()

        

        btnContar.pack(side=RIGHT, padx=2, pady=2)
        btnParar.pack(side=RIGHT, padx=3, pady=2)
        btnCerrar.pack(side=RIGHT, padx=4, pady=2)
        output.pack()

        self.contando=True
        self.timer = Timer(1, self.contar)
        self.timer.start()

    def contar(self):
        
        print(self.contando)
        if self.contando==True:
            self.contador.contar()
            #print(self.contador.mostrarConteo())
        else:
            None
            #print(self.contador.mostrarConteo())
        time.sleep(1)
        self.contar()
        #threading.Timer(1, self.contar()).start()
        
        
        
    
    def detener(self):
        self.contando=False

    def iniciar(self):
        self.contando=True
    
    def cerrar(self):
        self.timer.cancel()

    def elegirSistema(self):
        print("Eleccion" + self.opcion)
