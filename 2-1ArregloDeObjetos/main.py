from Contacto import Contacto

if __name__ == '__main__':
    contactos = []

    #Se crea un contacto y se agrega a la lista
    contactos.append(Contacto())
    contactos[0].setNombre("Juan")
    contactos[0].setApellido("Diaz")
    contactos[0].setTelefono("2334567")

    #Se crea el segundo contacto y se agrega a la lista
    contactos.append(Contacto())
    contactos[1].setNombre("Miguel")
    contactos[1].setApellido("Mendez")
    contactos[1].setTelefono("2378907")

    for contacto in contactos:
        print(contacto.getApellido()," ",contacto.getNombre()," ",contacto.getTelefono())