from abc import ABC, abstractmethod   ##Clase abstracta

class Sistema(ABC):

    __base = 0

    def __init__(self):
        self._numeroA = 0
        self._numeroB = 0
        self._resultado = 0
        self._operacion= ' '


    def set_numeroA (self, n):
        self._numeroA = n

    def set_numeroB (self, n):
        self._numeroB = n

    def set_resultado (self, n):
        self._resultado = n

    def set_operacion (self, o):
        self._operacion = o

    def get_numeroA(self):
        return self._numeroA

    def get_numeroB(self):
        return self._numeroB

    def get_resultado(self):
        return self._resultado

    def get_operacion(self):
        return self._operacion

    def suma(self):
        return self._numeroA + self._numeroB

    def resta(self):
        return self._numeroA - self._numeroB

    def multiplicacion(self):
        return self._numeroA * self._numeroB

    def division(self):
        return self._numeroA / self._numeroB

    def establecerNumeroA(self, a):
        n = int(a, self._base)
        self.set_numeroA(n)

    def establecerNumeroB(self, b):
        n = int(b, self._base)
        self.set_numeroA(n)

    def retornarNumeroA(self):
        cad  =""
        if self.__base == 2:
            cad = str(format(self._numeroA, "b"))
        elif self.__base == 8:
            cad = str(format(self._numeroA, "o"))
        elif self.__base == 10:
            cad = str(format(self._numeroA, "d"))
        elif self.__base == 16:
            cad = str(format(self._numeroA, "x"))
        return cad

    def retornarNumeroB(self):
        cad  =""
        if self.__base == 2:
            cad = str(format(self._numeroB, "b"))
        elif self.__base == 8:
            cad = str(format(self._numeroB, "o"))
        elif self.__base == 10:
            cad = str(format(self._numeroB, "d"))
        elif self.__base == 16:
            cad = str(format(self._numeroB, "x"))
        return cad

    def retornarResultado(self):
        cad  =""
        if self.__base == 2:
            cad = str(format(self._resultado, "b"))
        elif self.__base == 8:
            cad = str(format(self._resultado, "o"))
        elif self.__base == 10:
            cad = str(format(self._resultado, "d"))
        elif self.__base == 16:
            cad = str(format(self._resultado, "x"))
        return cad

class Binario(Sistema):
    def __init__(self):
        self.__base = 2


class Conversion():
    
    def fromHexadecimal(cad):
        return int(cad, 16)


    def fromOctal(cad):
        return int(cad, 8)

    
