import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        #print("Se ha creado una persona nueva con el nombre de {}.".format(self.nombre)
        print(f"Se ha creado una persona nueva con el nombre de {self.nombre}.")

    def __str__(self):
        #return "Nombre: {} \nGénero: {} \nEdad: {}".format(self.nombre, self.genero, self.edad)
        return f"Nombre: {self.nombre} \nGénero: {self.genero} \nEdad: {self.edad}"

class ListaPersonas():

    personas=[]

    def __init__(self):
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            # print ("Se ha cargado {} personas del fichero externo.".format(self.personas)
            print(f"Se ha cargado {len(self.personas)} personas del fichero externo.")

        except:
            print("El fichero está vacío.")

        finally:
            listaDePersonas.close()
            del listaDePersonas

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasFicherosExerno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasFicherosExerno (self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del listaDePersonas

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

p03=Persona("Ana", "Mujer", 19)
miLista.agregarPersonas(p03)

miLista.mostrarInfoFicheroExterno()
