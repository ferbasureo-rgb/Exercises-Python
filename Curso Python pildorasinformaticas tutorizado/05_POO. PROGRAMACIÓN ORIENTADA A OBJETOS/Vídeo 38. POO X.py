from Tools.scripts.stable_abi import binutils_get_exported_symbols


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
        Persona.__init__(self, nombre, apellido, edad)
        self.escuela = escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "\nEscuela: "  + self.escuela

    def estudia(self):
        return self.nombre + " está estudiando."

class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad, empresa):
        Persona.__init__(self, nombre, apellido, edad)
        self.empresa = empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "\nEmpresa: " + self.empresa

    def trabaja(self):
        return self.nombre + " está trabajando."

class Director(Trabajador, Estudiante): #El orden en el que se indica la clase heredada importa, se da una preferencia al que va primero.
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.bonus = bonus

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "\nBonus: " + str(self.bonus)

    def dirigir(self):
        return self.nombre + " está dirigiendo la empresa" + self.empresa + " ."


persona01 = Persona("Javier", "Rodríguez", 18)
estudiante01 = Estudiante("Jim", "Carrey", 65, "UMA")

print(persona01.getDatosPersonales())
print(estudiante01.getDatosPersonales())
print("------")

trabajador01 = Trabajador("Juanlu", "López", 55, "Eiffage")
print(trabajador01.getDatosPersonales())

director01 = Director("Michael", "Scott", 46, "Dunder Mifflin", "Yale", 1500)
print(director01.getDatosPersonales())

