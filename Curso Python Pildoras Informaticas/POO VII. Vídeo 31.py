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
miMoto=Moto("Honda","CBR")
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia =100

    def cargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VElectricos, Vehiculos):
    def estado(self):
        super().estado()

miBici=BicicletaElectrica("Orbea", "HBD100")
miBici.estado()

print("""
--- Ejemplo persona (función super())---
      """)
class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad=f"{antigüedad} años."
    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} \nAntigüedad: {self.antigüedad}")


Antonio=Persona("Antonio", 19, "Málaga")
Antonio.descripcion()

Juan=Empleado(15000, 5, "Juan", 42, "Málaga")
Juan.descripcion()

print(isinstance(Antonio, Persona))





