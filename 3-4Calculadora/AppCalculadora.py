from Logica import Decimal, Conversion, Sistema, Binario, Octal, Hexadecimal
import tkinter  as tk 




class AppCalculadora():
    def __init__(self, root):
        self.s  =  10
        self.actual = self.s
        self.nuevo = 0
        self.d = Decimal()
        self.c = Conversion()
        self.sistema = Sistema()
        self.root = root
        self.root.geometry("500x500")
        self.master_frame = tk.Frame(root)

        self.txtEntrada = tk.Entry(root)
        self.txtEntrada.grid(column=3, row=0, sticky="W")
        tk.Radiobutton(root, text="BIN", value=2, command= lambda: self.elegirSistema(2), height = 1, width = 5).grid(column=1, row=1, sticky="W")
        tk.Radiobutton(root, text="OCT", value=8, command= lambda: self.elegirSistema(8)).grid(column=2, row=1, sticky="W")
        tk.Radiobutton(root, text="DEC",  value=10, command= lambda: self.elegirSistema(10)).grid(column=3, row=1, sticky="W")
        tk.Radiobutton(root, text="HEX",  value=16, command= lambda: self.elegirSistema(16)).grid(column=4, row=1, sticky="W")

        cont = 0
        
        self.btnF = tk.Button( text="F", command= lambda: self.write("F"), height = 1, width = 5)
        self.btnF.grid(column=3, row=2)
        self.btnE = tk.Button( text="E", command= lambda: self.write("E"), height = 1, width = 5 )
        self.btnE.grid(column=2, row=2)
        self.btnD = tk.Button( text="D", command= lambda: self.write("D"), height = 1, width = 5)
        self.btnD.grid(column=1, row=2)
        self.btnC = tk.Button( text="C", command= lambda: self.write("C"), height = 1, width = 5)
        self.btnC.grid(column=3, row=3)
        self.btnB = tk.Button( text="B", command= lambda: self.write("B"), height = 1, width = 5)
        self.btnB.grid(column=2, row=3)
        self.btnA = tk.Button( text="A", command= lambda: self.write("A"), height = 1, width = 5)
        self.btnA.grid(column=1, row=3)
        self.btn9 = tk.Button( text="9", command= lambda: self.write("9"), height = 1, width = 5)
        self.btn9.grid(column=3, row=4)
        self.btn8 = tk.Button( text="8", command= lambda: self.write("8"), height = 1, width = 5)
        self.btn8.grid(column=2, row=4)
        self.btn7 = tk.Button( text="7", command= lambda: self.write("7"), height = 1, width = 5)
        self.btn7.grid(column=1, row=4)
        self.btn6 = tk.Button( text="6", command= lambda: self.write("6"), height = 1, width = 5)
        self.btn6.grid(column=3, row=5)
        self.btn5 = tk.Button( text="5", command= lambda: self.write("5"), height = 1, width = 5)
        self.btn5.grid(column=2, row=5)
        self.btn4 = tk.Button( text="4", command= lambda: self.write("4"), height = 1, width = 5)
        self.btn4.grid(column=1, row=5)
        self.btn3 = tk.Button( text="3", command= lambda: self.write("3"), height = 1, width = 5)
        self.btn3.grid(column=3, row=6)
        self.btn2 = tk.Button(root, text="2", command= lambda: self.write("2"), height = 1, width = 5)
        self.btn2.grid(column=2, row=6)
        self.btn1 = tk.Button( text="1", command= lambda: self.write("1"), height = 1, width = 5)
        self.btn1.grid(column=1, row=6)
        self.btn0 = tk.Button( text="0", command= lambda: self.write("0"), height = 1, width = 10)
        self.btn0.grid(column=2, row=7)
        self.btnCI = tk.Button( text="CI", command= lambda: self.clear(), height = 1, width = 5)
        self.btnCI.grid(column=1, row=8)
        self.btnCE = tk.Button( text="CE", command= lambda: self.clear(), height = 1, width = 5)
        self.btnCE.grid(column=2, row=8)

        #OPERADORES
        self.btnDiv = tk.Button( text="/", command= lambda: self.operacion("/"), height = 1, width = 5)
        self.btnDiv.grid(column=4, row=2)
        self.btnMult = tk.Button( text="*", command= lambda: self.operacion("*"), height = 1, width = 5)
        self.btnMult.grid(column=4, row=3)
        self.btnResta = tk.Button( text="-", command= lambda: self.operacion("-"), height = 1, width = 5)
        self.btnResta.grid(column=4, row=4)
        self.btnSuma = tk.Button( text="+", command= lambda: self.operacion("+"), height = 1, width = 5)
        self.btnSuma.grid(column=4, row=5)
        self.btnIgual = tk.Button( text="=", command= lambda: self.calcular("="), height = 1, width = 5)
        self.btnIgual.grid(column=4, row=6)

    def elegirSistema(self, value):
        self.actual = self.s
        self.nuevo = value
        if value == 2:
            self.sistema = Binario()
            self.btn2["state"] = tk.DISABLED
            self.btn3["state"] = tk.DISABLED
            self.btn4["state"] = tk.DISABLED
            self.btn5["state"] = tk.DISABLED
            self.btn6["state"] = tk.DISABLED
            self.btn7["state"] = tk.DISABLED
            self.btn8["state"] = tk.DISABLED
            self.btn9["state"] = tk.DISABLED
            self.btnA["state"] = tk.DISABLED
            self.btnB["state"] = tk.DISABLED
            self.btnC["state"] = tk.DISABLED
            self.btnD["state"] = tk.DISABLED
            self.btnE["state"] = tk.DISABLED
            self.btnF["state"] = tk.DISABLED
        elif value == 8:
            self.btn2["state"] = tk.ACTIVE
            self.btn3["state"] = tk.ACTIVE
            self.btn4["state"] = tk.ACTIVE
            self.btn5["state"] = tk.ACTIVE
            self.btn6["state"] = tk.ACTIVE
            self.btn7["state"] = tk.ACTIVE
            self.btn8["state"] = tk.DISABLED
            self.btn9["state"] = tk.DISABLED
            self.btnA["state"] = tk.DISABLED
            self.btnB["state"] = tk.DISABLED
            self.btnC["state"] = tk.DISABLED
            self.btnD["state"] = tk.DISABLED
            self.btnE["state"] = tk.DISABLED
            self.btnF["state"] = tk.DISABLED
           
        elif value == 10:
            self.sistema =Decimal()
            self.btn2["state"] = tk.ACTIVE
            self.btn3["state"] = tk.ACTIVE
            self.btn4["state"] = tk.ACTIVE
            self.btn5["state"] = tk.ACTIVE
            self.btn6["state"] = tk.ACTIVE
            self.btn7["state"] = tk.ACTIVE
            self.btn8["state"] = tk.ACTIVE
            self.btn9["state"] = tk.ACTIVE
            self.btnA["state"] = tk.DISABLED
            self.btnB["state"] = tk.DISABLED
            self.btnC["state"] = tk.DISABLED
            self.btnD["state"] = tk.DISABLED
            self.btnE["state"] = tk.DISABLED
            self.btnF["state"] = tk.DISABLED
        elif value == 16:
            self.sistema =Hexadecimal()
            self.btn2["state"] = tk.ACTIVE
            self.btn3["state"] = tk.ACTIVE
            self.btn4["state"] = tk.ACTIVE
            self.btn5["state"] = tk.ACTIVE
            self.btn6["state"] = tk.ACTIVE
            self.btn7["state"] = tk.ACTIVE
            self.btn8["state"] = tk.ACTIVE
            self.btn9["state"] = tk.ACTIVE
            self.btnA["state"] = tk.ACTIVE
            self.btnB["state"] = tk.ACTIVE
            self.btnC["state"] = tk.ACTIVE
            self.btnD["state"] = tk.ACTIVE
            self.btnE["state"] = tk.ACTIVE
            self.btnF["state"] = tk.ACTIVE
        self.s = value
        numero = self.txtEntrada.get()
        self.txtEntrada.delete(0, tk.END)
        self.txtEntrada.insert(0, self.c.convertirSistema(self.actual,self.nuevo, numero))


    def write(self, value):
        print(value)
        self.txtEntrada.insert(0, value)

    def clear(self):
        self.txtEntrada.delete(0, tk.END)

    def operacion(self, value):
        number = self.txtEntrada.get()
        self.txtEntrada.delete(0, tk.END)
        self.d.set_operacion(value)
        if self.s == 2:
            self.d.establecerNumeroA(number)
        if self.s == 8:
            self.d.set_numeroA(self.c.fromOctal(number))
        if self.s == 10:
            self.d.establecerNumeroA(number)
        if self.s == 16:
            self.d.set_numeroA(self.c.fromHexadecimal(number))

    def calcular(self, value):
        number = self.txtEntrada.get()
        self.txtEntrada.delete(0, tk.END)
        if self.s == 2:
            self.d.establecerNumeroB(number)
        elif self.s == 8:
            self.d.set_numeroB(self.c.fromOctal(number))
        elif self.s == 10:
            self.d.establecerNumeroB(number)
        elif self.s == 16:
            self.d.set_numeroB(self.c.fromHexadecimal(number))

        operacion = self.d.get_operacion()
        if operacion == "+":
            self.d.suma()
        elif operacion == "-":
            self.d.resta()
        elif operacion == "*":
            self.d.multiplicacion()
        elif operacion == "/":
            self.d.division()
        
        if self.s == 2:
            self.txtEntrada.insert(0, self.c.toBinario(self.d.get_resultado()))
        elif self.s == 8:
            self.txtEntrada.insert(0,self.c.toOctal(self.d.get_resultado()))
        elif self.s == 10:
            self.txtEntrada.insert(0,str(self.d.get_resultado()))
        elif self.s == 16:
            self.txtEntrada.insert(0,self.c.toHexadecimal(self.d.get_resultado()))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCalculadora(root)
    root.mainloop()


    
    c = Conversion()
    print(c.convertirSistema(16, 16, '12'))
