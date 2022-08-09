from logica.Teclado import Teclado

if __name__ == '__main__':
    #Crea el objeto Teclado
    teclado = Teclado()

    #Le pide a teclado que lea una cadena que sera el nombre
    print("Ingresa tu nombre")
    nombre = teclado.capturarCadena()
    palabras = nombre.split()

    #desordena el nombre
    temp = ""
    palabras.reverse()
    for i in range(0, len(palabras)-1):
        temp = palabras[i]
        palabras[i] = palabras[i+1] + " "
        palabras[i+1] = temp

    #Guarda en un string la lista de palabras desordenadas
    nombreDesordenado = ""
    for palabra in palabras:
        nombreDesordenado += palabra + " "
    
    #Imprime el nombre desordenado
    print("Lo siento no entendi, su nombre es ", nombreDesordenado)

    #Le pide al teclado recibir numeros
    numeroEntero = 0
    precioBajito = 0.0
    precioAlto = 0.0
    print(type(precioAlto))

    print("podria indicarme cuantos años tiene?")
    teclado.capturarNumero(numeroEntero)
    print("podria decirme un precio aproximado del dolar?")
    teclado.capturarNumero(precioBajito)
    print("podria ahora decirme cuantos pesos son 1000 dolares?")
    teclado.capturarNumero(precioAlto)

    #Como es sordo no escucho (guardo) los datos anteriores
    print("a ver si capte bien");
    print("usted tiene mas o menos ",precioBajito," años");
    print("y 1000 dolares son ",numeroEntero," pesos a ",precioAlto," pesos por dolares!");
    print("no, creo que no entendi");