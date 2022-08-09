class Contacto:
    # Con raya al piso (_) se declara
    # un atributo privado
    _nombre = ""
    _apellido = ""
    _telefono = ""
    _prueba = "hola"

    def getApellido(self):
        return self._apellido

    def setApellido(self, apellido):
        self._apellido = apellido

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getTelefono(self):
        return self._telefono

    def setTelefono(self, telefono):
        self._telefono = telefono