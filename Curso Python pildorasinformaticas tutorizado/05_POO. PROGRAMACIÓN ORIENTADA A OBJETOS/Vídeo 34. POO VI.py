class Persona():
    __nombre=""
    __apellido= ""
    __edad=0
    genero="Sin definir"
    # Constructor
    def __init__(self, nombre, apellido, genero):
        self.__nombre=nombre
        self.__apellido=apellido
        self.genero=genero

    # Métodos de acceso: setters (establecer los valores de la propiedad) y getters (acceder a qué valor hay almacenado en esa propiedad)
    # Creo un setters, por convención empieza por set. Se puede poner en cualquier sitio dentro de la clase.
    def setEdad(self, edad):
        try:
            if edad < 0 or edad > 110:
                raise ValueError ("Error en la edad")

            else:
                self.__edad=edad
                return self.__edad
        except ValueError:
            print("Error en la edad. Por favor, introduzca un valor válido")

    #Métodos:
    def habla(self):

        return "La persona que se llama " + self.__nombre + " está hablando."

    def camina(self):
        return "La persona que se llama" + self.__nombre + " está caminando."

    def getDatos(self):
        return "Nombre: " + self.__nombre + " Apellido: " + self.__apellido + \
            " Edad: " + str(self.__edad) + " Género: " + self.genero

p1=Persona("Pedro", "Ramírez", "Masculino")

print(p1.getDatos())

p1.__apellido= "Jiménez"
p1.setEdad(52)

print(p1.getDatos())

p2=Persona ("Nuria", "Domínguez", "Femenino")
p2.setEdad(-7)
print(p2.getDatos())