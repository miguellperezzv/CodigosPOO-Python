import tkinter  as tk 
from tkinter import Canvas
from lineasdibujables_logica import *


class GUI():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.master_frame = tk.Frame(root)
        mi_Canvas = miCanvas()
        mi_Canvas.bind("<Button-1>", self.mouseClicked)

    def mouseClicked(self,event):
        print("clicked")
        
        
class miCanvas(Canvas):
    

    def __init__(self):
        self.enOrigen = True
        self.origen = Punto(0,0)
        self.fin = Punto(0,0)
        self.lineas = []
        self.background = "green"
        

    def addLinea(self, linea):
        self.lineas.add(linea)

    #override
    def paint(self):
        for linea in self.lineas:
            linea.dibujar(self)
