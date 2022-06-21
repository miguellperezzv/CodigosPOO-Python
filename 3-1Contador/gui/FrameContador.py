import tkinter  as tk
from threading import Timer
import threading
from logica.ContadorOctal import ContadorOctal
import time




class FrameContador:

    contando = False
    contador = ContadorOctal()
    
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x200")
        self.master_frame = tk.Frame(root)
        self.master_frame.pack(fill=tk.BOTH, expand=True)
        self.root.title("Contador")
        btnContar = tk.Button(self.master_frame, text="Contar", command= self.iniciar)
        btnParar = tk.Button(self.master_frame, text="Parar", command= self.detener)
        btnContar.pack()
        btnParar.pack()
        self.contando=True
        Timer(1, self.contar).start()
        
        
        
        
        
        
        

    def contar(self):


        if self.contando==True:
            self.contador.contar()
            print(self.contador.mostrarConteo())
        else:
            print(self.contador.mostrarConteo())
        time.sleep(1)
        self.contar()
        #threading.Timer(1, self.contar()).start()
        
        
        
    
    def detener(self):
        self.contando==False

    def iniciar(self):
        self.contando==True


