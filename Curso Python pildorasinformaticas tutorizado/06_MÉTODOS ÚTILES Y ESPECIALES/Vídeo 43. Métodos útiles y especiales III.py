class Persona():

    def __init__(self, nom, ape, edad):
        self.nombre=nom
        self.apellido=ape
        self.edad=edad

    #def __str__(self):
        #return "Datos de la persona: \nNombre: " + self.nombre+ "\nApellido: "+ self.apellido + "\nEdad: "+ str(self.edad)

    def __repr__(self):
        return "Datos de la persona: \nNombre: " + self.nombre+ "\nApellido: "+ self.apellido + "\nEdad: "+ str(self.edad)

p1=Persona("Jimmy","Hendrix",26)
print(p1)

import datetime

hoy = datetime.date.today()
print(repr(hoy))

class Agenda():
    def __init__(self):
        self.miAgenda={}

    def __len__(self):
        return len(self.miAgenda)

    def agregarPersona(self, nombre, telefono):
        self.miAgenda[nombre]=telefono

agendaPersonal = Agenda()

agendaPersonal.agregarPersona("Juan", "638938950")

print(len(agendaPersonal))