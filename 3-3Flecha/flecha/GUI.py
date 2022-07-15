from tkinter import *
from Flecha import Flecha
import os

class GUI:

    canvas = None
    f = Flecha()

    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        #self.master_frame = tk.Frame(root)
        self.canvas=Canvas(self.root, width=500, height=500, background="white")
    
        self.f.setImagen('..\\imagenes\\flecha_up.png')
        self.f.setCoordX(10)
        self.f.setCoordY(23)
        self.canvas.grid(column=0, row=0)
        self.canvas.pack()
        img=PhotoImage(file=self.f.getImagen())
        print("RUTA DE LA IMAGEN " + str(self.f.getImagen()))
        #self.create_image(30, 100, image=archi1, anchor="nw")
        self.canvas.create_image(self.f.getCoordX(), self.f.getCoordY(), image=img, anchor=NW)