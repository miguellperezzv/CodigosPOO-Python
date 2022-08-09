class Teclado:

    def capturarCadena(self):
        cadena = ""
        try:
            cadena = input()
        except:
            print("Error en la entrada")

        return cadena
    
    #Sobre carga de metodos con el if entero, o flotante, double no es posible en python
    def capturarNumero(self, numero):
        n = 0
        try:
            if isinstance(numero, int):
                n = int(input())
            elif isinstance(numero, float):
                n = float(input())
        except ValueError:
            print("Error en el formato numérico")
        except:
            print("Error en la entrada")
