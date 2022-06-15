

from abc import ABC, abstractmethod

class Contador(ABC):

    tope = 0
    valor = 0
    

    #Constructor
    def __init__(self):
        self.valor = 0
        self.tope = 4098

    def contar(self):
        if (self.valor  < self.tope) :
            self.valor = self.valor + 1
        else:
            self.valor = 0
    
    @abstractmethod
    def mostrarConteo(self):
        pass

