from logica.ContadorBinario import ContadorBinario 
from logica.ContadorDecimal import ContadorDecimal
from logica.ContadorHexadecimal import ContadorHexadecimal
from logica.ContadorOctal import ContadorOctal
from gui.FrameContador import FrameContador
import tkinter as tk


root = tk.Tk()
app = FrameContador(root)



if __name__ == "__main__":
    contador = ContadorHexadecimal()
    limite=4099;   
    
    '''
    for i in range(limite):
        contador.contar()
        print(contador.mostrarConteo())
    '''
    
    
    #root.protocol("WM_DELETE_WINDOW", app.timer.cancel())
    root.mainloop()
    


        


 
