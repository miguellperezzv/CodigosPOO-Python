class Teclado:

    #Lee una cadena de caracteres
    def capturarCadena(self):
        cadena = ""
        try:
            cadena = input()
        except:
            print("Error en la entrada")

        return cadena

    #Obtiene el peso de la cadena teniendo en cuenta su valor en ascii
    def calcularPeso(self, cadena):
        peso = 0
        for caracter in cadena:
            #ord obtiene el valor del caracter en ascii
            peso += ord(caracter)

        return peso

if __name__ == "__main__":
    cadena1 = ""
    cadena2 = ""
    teclado = Teclado()

    while True:
        print("Ingrese dos cadenas")
        cadena1 = teclado.capturarCadena()
        cadena2 = teclado.capturarCadena()

        #Si ambos pesos son iguales se rompe el ciclo
        if teclado.calcularPeso(cadena1) == teclado.calcularPeso(cadena2):
            break


        