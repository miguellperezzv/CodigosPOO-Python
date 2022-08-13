import math
import tkinter as tk

class Linea():
    def __init__(self,origen,fin):
        self._origen = origen
        self._fin = fin

    def calcularDistancia(self):
        distancia = math.sqrt(math.pow((self._origen.getX()- self._origen.getX()),2) + math.pow((self._origen.getY()- self._origen.getY()),2))
        return distancia

    def dibujar(self,canva):
        canva.create_line(self._origen.getX(), self._origen.getY(), self._fin.getX(), self._fin.getY())
        canva.create_text(self._origen.getX(), self._origen.getY(), anchor=tk.W, text=str(self.calcularDistancia()))
        
class Punto():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y