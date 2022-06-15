

from logica.Contador import Contador

class ContadorBinario(Contador):

    def mostrarConteo(self):
        return "{0:b}".format(self.valor)
        
        
