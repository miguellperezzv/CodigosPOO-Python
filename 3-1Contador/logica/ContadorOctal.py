from logica.Contador import Contador

class ContadorOctal(Contador):

    def mostrarConteo(self):
        return oct(self.valor).replace("0o","")