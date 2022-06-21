from logica.ContadorBinario import ContadorBinario 
from logica.ContadorDecimal import ContadorDecimal
from logica.ContadorHexadecimal import ContadorHexadecimal
from logica.ContadorOctal import ContadorOctal
from gui.FrameContador import FrameContador
import tkinter as tk




if __name__ == "__main__":
    contador = ContadorHexadecimal()
    limite=4099;   
    """
    for i in range(limite):
        contador.contar()
        #print(contador.mostrarConteo())
    """
    
    root = tk.Tk()
    app = FrameContador(root)
    root.mainloop()
    
        


 
