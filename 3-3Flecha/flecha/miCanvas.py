from tkinter import Canvas
from Flecha import Flecha
import tkinter as tk

class miCanvas(Canvas):
    f = Flecha()
    f.setImagen("imagenes/flecha_up.png")
    f.setCoordX(10)
    f.setCoordY(23)
    
    def __init__(self):
        self.width = 500
        self.height = 500
        self.background = "black"
        self.pack()

    def paint(self):
        #self.img = Image.open(self.f.getImagen()) 
        #self.imgCanva = ImageTk.PhotoImage(self.img)
        img=tk.PhotoImage(file=self.f.getImagen())
        self.create_image(30, 100, image=img, anchor="nw")
        #self.create_image(self.f.getCoordX(), self.f.getCoordY(), image=img, anchor = "nw")