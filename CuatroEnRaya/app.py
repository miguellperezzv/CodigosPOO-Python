from logica.Tablero import Tablero

juego = Tablero()
def jugar():
    turno = 1
    while turno <=9:
        x, y =  (input().split(" "))
        x = int(x)
        y = int(y)
        if x >= 0 and x <=2 and y>=0 and y<=2:
            if turno%2 !=0:
                if juego.verificarVacio(x, y):
                    juego.getTablero()[x][y].setForma("X")
                    juego.ver()
                    if juego.validarGanador():
                        print("Hay Ganador X")
                        turno = 10
                    turno += 1
            else:
                if juego.verificarVacio(x,y):
                    juego.getTablero()[x][y].setForma("O")
                    juego.ver()
                    if juego.validarGanador():
                        print("Hay Ganador X")
                        turno = 10
                    turno += 1
        else:
            print("X o Y fuera de rango ")

                   
        

if __name__ == "__main__":
    juego.llenar()
    juego.ver()
    jugar()


