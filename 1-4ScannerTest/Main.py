if __name__ == '__main__':
    x = int(input("Ingrese un número entero: "))
    palabra = input("Ingrese una frase: ")
    
    #Conversión obligada de tipo para x (int->string)
    print(palabra + str(x))
