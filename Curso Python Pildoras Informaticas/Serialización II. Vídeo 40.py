import pickle

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")

coche01=Vehiculos("Mazda", "MX5")
coche02=Vehiculos("Seat", "Panda")
coche03=Vehiculos("Renault", "19")

coches = [coche01, coche02, coche03]

fichero = open("losCoches", "wb")
pickle.dump(coches, fichero)

fichero.close()

del fichero

ficheroApertura=open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())