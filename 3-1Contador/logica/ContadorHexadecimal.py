from logica.Contador import Contador

class ContadorHexadecimal(Contador):

    def mostrarConteo(self):
        return "{0:02X}".format(self.valor)