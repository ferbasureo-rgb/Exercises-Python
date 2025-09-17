class Motorizado():
    def __init__(self, marca):
        self.marca = marca
    def estado(self):
        print("El coche está nuevo.")
class Coche(Motorizado):
    def __init__(self, marca):
        super().__init__(marca)
        self.__ruedas = 4
    def desplazamiento(self):
        print(f"Es un {self.marca} y se desplaza con {self.__ruedas} ruedas.")

class Moto(Motorizado):
    def __init__(self, marca):
        super().__init__(marca)
        self.__ruedas = 2
    def desplazamiento(self):
        print(f"Es un {self.marca} y se desplaza con {self.__ruedas} ruedas.")

class Triciclo(Motorizado):
    def __init__(self, marca):
        super().__init__(marca)
        self.__ruedas = 3
    def desplazamiento(self):
        print(f"Es un {self.marca} y se desplaza con {self.__ruedas} ruedas.")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto("Volvo")

desplazamientoVehiculo(miVehiculo)

miVehiculo.estado()