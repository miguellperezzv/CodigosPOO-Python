from logica.Ficha import Ficha

class Tablero():
    __tablero = [[ [] for j in range(3)] for i in range(3)]


    def getTablero(self):
        return self.__tablero

    def setTablero(self, tablero):
        self.__tablero = tablero

    def llenar(self):
        for i in range(3):
            for j in range(3):
                self.__tablero[i][j]=Ficha()
                self.__tablero[i][j].setForma("-")

    def ver(self):
        tablero = ""
        for i in range(3):
            for j in range(3):
                tablero += (self.__tablero[i][j].getForma()+" \t")
            tablero += ("\n")
        print(tablero)

    def verificarVacio(self, x, y):
        if self.__tablero[x][y].getForma() == "-":
            return True
        else:
            return False 
    
    def validarFilas(self):
        for i in range(3):
            if (self.__tablero[i][0].getForma() and self.__tablero[i][1].getForma() and self.__tablero[i][2].getForma()) == ("X" or 'Y'):
                return True
            else:
                return False
    
    def validarColumnas(self):
        for i in range(3):
            if (self.__tablero[0][i].getForma() and self.__tablero[1][i].getForma() and self.__tablero[2][i].getForma()) == ("X" or 'Y'):
                return True
            else:
                return False

    def validarGanador(self):
        bandera = self.validarFilas()
        if not bandera:
            bandera = self.validarColumnas()
        return bandera