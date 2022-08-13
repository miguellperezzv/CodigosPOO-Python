from abc import ABC, abstractmethod   ##Clase abstracta

class Sistema(ABC):

    

    def __init__(self):
        self._numeroA = 0
        self._numeroB = 0
        self._resultado = 0
        self._operacion= ' '
        self._base=0


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
        self._resultado = self._numeroA + self._numeroB

    def resta(self):
        self._resultado =  self._numeroA - self._numeroB

    def multiplicacion(self):
        self._resultado =  self._numeroA * self._numeroB

    def division(self):
        self._resultado =  self._numeroA / self._numeroB

    def establecerNumeroA(self, a):
        n = int(a, self._base)
        self.set_numeroA(n)

    def establecerNumeroB(self, b):
        n = int(b, self._base)
        self.set_numeroB(n)

    def retornarNumeroA(self):
        cad  =""
        if self._base == 2:
            cad = str(format(self._numeroA, "b"))
        elif self._base == 8:
            cad = str(format(self._numeroA, "o"))
        elif self._base == 10:
            cad = str(format(self._numeroA, "d"))
        elif self._base == 16:
            cad = str(format(self._numeroA, "x"))
        return cad

    def retornarNumeroB(self):
        cad  =""
        if self._base == 2:
            cad = str(format(self._numeroB, "b"))
        elif self._base == 8:
            cad = str(format(self._numeroB, "o"))
        elif self._base == 10:
            cad = str(format(self._numeroB, "d"))
        elif self._base == 16:
            cad = str(format(self._numeroB, "x"))
        return cad

    def retornarResultado(self):
        cad  =""
        if self._base == 2:
            cad = str(format(self._resultado, "b"))
        elif self._base == 8:
            cad = str(format(self._resultado, "o"))
        elif self._base == 10:
            cad = str(format(self._resultado, "d"))
        elif self._base == 16:
            cad = str(format(self._resultado, "x"))
        return cad

class Binario(Sistema):
    def __init__(self):
        self._base = 2

class Decimal(Sistema):
    def __init__(self):
        self._base = 10

class Octal(Sistema):
    def __init__(self):
        self._base = 8

class Hexadecimal(Sistema):
    def __init__(self):
        self._base = 16


class Conversion():
    
    def fromHexadecimal(self,cad):
        return int(cad, 16)

    def fromOctal(self,cad):
        return int(cad, 8)

    def fromBinario(self, cad):
        return int(cad, 2)

    def toHexadecimal(self, n):
        return str(format(n, "x"))

    def toOctal(self, n):
        return str(format(n, "o"))

    def toBinario(self, n):
        return str(format(n, "b"))

    def convertirSistema(self,actual, nuevo, cad):
        res = ""
        num = 0
        if len(cad) > 0:
            if actual == 2:
                num = self.fromBinario(cad)
            elif actual == 8:
                num = self.fromOctal(cad)
            elif actual == 10:
                num = int(cad)
            elif actual == 16:
                num = self.fromHexadecimal(cad)
        if nuevo == 2:
            res = self.toBinario(num)
        elif nuevo == 8 : 
            res = self.toOctal(num)
        elif nuevo == 10:
            res = str(num)
        elif nuevo == 16:
            res  = self.toHexadecimal(num)
        return res
    
