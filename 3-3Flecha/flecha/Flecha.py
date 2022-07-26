import os 
class Flecha:


    imagen = ""
    coordenadaX = 0
    coordenadaY = 0

    def getCoordX(self):
        return self.coordenadaX

    def getCoordY(self):
        return self.coordenadaY
    
    def setCoordX(self,coord):
        self.coordenadaX = (int) (coord)
    
    def setCoordY(self,coord):
        self.coordenadaY = int (coord)

    def getImagen(self):
        #print("RUTA "+ self.imagen)
        return self.imagen

    def setImagen(self, string):
        
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, string)
        self.imagen = absolute_image_path
    