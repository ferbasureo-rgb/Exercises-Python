class Persona:

    def hablar(self):
        return "Hablo como una persona."

class Trabajador(Persona):
    def hablar(self):
        return "Hablo como un trabajador."

class Director(Trabajador):
    def hablar(self):
        return "Hablo como un director."

def hazlesHablar(listaDeLasPersonas):
    for persona in listaDeLasPersonas: #Persona va a ir cambiando de forma: polimorfismo. Se va a transformar en Persona, Trabajardo y Director.
        print(persona.hablar())



Antonio = Persona()
Ana = Trabajador()
Maria = Director()

print(Antonio.hablar())
print(Ana.hablar())
print(Maria.hablar())


print("---")

listaPersonas = [Antonio, Ana, Maria]

hazlesHablar(listaPersonas)




