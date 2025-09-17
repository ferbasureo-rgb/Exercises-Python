class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # get es convención para getters:
    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + "\nApellido: " + self.apellido + " \nEdad: " + str(self.edad)

    def habla(self):
        return self.nombre + " está hablando."

    def piensa(self):
        return self.nombre + " está pensando."

    def camina(self):
        return self.nombre + " está caminando."

    def come(self):
        return self.nombre + " está comiendo."

class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, escuela):
        super().__init__(nombre, apellido, edad)
        self.escuela = escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "\nEscuela: "  + self.escuela

    def estudia(self):
        return self.nombre + " está estudiando."



persona01 = Persona("Javier", "Rodríguez", 18)


estudiante01 = Estudiante("Jim", "Carrey", 65, "UMA")

print(persona01.getDatosPersonales())
print(estudiante01.getDatosPersonales())




