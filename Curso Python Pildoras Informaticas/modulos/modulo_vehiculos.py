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



class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Puede hacer el caballito."
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena} \nHace caballito: {self.hcaballito}")

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta está cargada."
        else:
            return "La furgoneta no está cargada."

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia =100

    def cargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VElectricos, Vehiculos):
    def estado(self):
        super().estado()





