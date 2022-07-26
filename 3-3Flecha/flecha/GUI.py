from tkinter import *
from Flecha import Flecha
import os
import tkinter as tk

class GUI:
    
    def mouseClicked(self,event):
        self.canvas1.delete("all")
        f = Flecha()
        f.setImagen("..\\imagenes\\flecha_up.png")
        f.setCoordX(event.x)
        f.setCoordY(event.y)
        self.archi1=tk.PhotoImage(file=f.getImagen())
        self.canvas1.create_image(f.getCoordX(), f.getCoordY(), image=self.archi1, anchor="nw")

    def keyPressed(self,event):
        #print(event)
        f = Flecha()
        f.setCoordX(event.x)
        f.setCoordY(event.y)
        if event.keysym == "Up":
           f.setImagen("..\\imagenes\\flecha_up.png")
        if event.keysym == "Down":
            f.setImagen("..\\imagenes\\flecha_down.png")
        if event.keysym == "Left":
            f.setImagen("..\\imagenes\\flecha_left.png")
        if event.keysym == "Right":
            f.setImagen("..\\imagenes\\flecha_right.png")
        self.canvas1.delete("all")
        self.archi1=tk.PhotoImage(file=f.getImagen())
        self.canvas1.create_image(f.getCoordX(), f.getCoordY(), image=self.archi1, anchor="nw")

    def __init__(self, root):
        f = Flecha()
        f.setImagen("..\\imagenes\\flecha_up.png")
        f.setCoordX(10)
        f.setCoordY(23)
        self.ventana1=root
        self.canvas1=tk.Canvas(self.ventana1, width=700, height=500, background="white")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.bind("<Button-1>", self.mouseClicked)
        self.canvas1.bind("<Key>", self.keyPressed)
        self.ventana1.bind("<Key>", self.keyPressed)
        self.archi1=tk.PhotoImage(file=f.getImagen())
        self.canvas1.create_image(int (f.getCoordX()), int (f.getCoordY()), image=self.archi1, anchor="nw")

    

    