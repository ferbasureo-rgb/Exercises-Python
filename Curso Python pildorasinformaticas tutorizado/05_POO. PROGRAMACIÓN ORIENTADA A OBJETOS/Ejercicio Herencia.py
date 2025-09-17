class Vehiculo():
    def __init__(self, color, ruedas, ancho, alto, marchas, asientos):
        self.color = color
        self.ruedas = ruedas
        self.ancho= ancho
        self.alto= alto
        self.marchas= marchas
        self.asientos= asientos
        self.acelerar = False
        self.frenar = False
        self.girar = False

    def Acelerar(self):
        print("El vehículo está acelerando.")
        self.acelerar = True

    def Frenar(self):
        print("El vehículo está frenando.")
        self.frenar = True

    def Girar(self):
        print("El vehículo está girando.")

    def getAtributos(self):
        print("--- ATRIBUTOS ---")
        print("Color:", self.color)
        print("Ruedas:", self.ruedas)
        print("Ancho:", self.ancho)
        print("Alto:", self.alto)
        print("Marchas:", self.marchas)
        print("Asientos:", self.asientos)

    def getAcciones(self):
        print("--- ACCIONES ---")
        print("El vehículo está acelerando :" + str(self.acelerar))
        print("El vehículo está frenando :" + str(self.frenar))
        print("El vehículo está girando :" + str(self.girar))


class Coche(Vehiculo):
    def __init__(self, color, ruedas, ancho, alto, marchas, asientos, cilindrada, aireacondicionado):
        super().__init__(color, ruedas, ancho, alto, marchas, asientos)
        self.cilindrada = cilindrada
        self.aireacondicionado = aireacondicionado

        self.arrancar = False
        self.marchaAtras= False

    def Arrancar(self):
        print("El vehículo está arrancado.")
        self.arrancar = True

    def MarchaAtras(self):
        print("El vehículo va marcha atrás.")
        self.marchaAtras = True

    def getAtributos(self):
        super().getAtributos()
        print("Cilindrada :", str(self.cilindrada))
        print("Aire Acondicionado:" + str(self.aireacondicionado))

    def getAcciones(self):
        super().getAcciones()
        print("El vehículo está arrancado: " + str(self.arrancar))
        print("El vehículo va marcha atrás: " + str(self.marchaAtras))

class Furgoneta(Coche):
    def __init__(self, color, ruedas, ancho, alto, marchas, asientos, cilindrada, aireacondicionado, carga):
        super().__init__(color, ruedas, ancho, alto, marchas, asientos, cilindrada, aireacondicionado)
        self.carga = carga

        self.cargar = False

    def Cargar(self):
        print("El vehículo va está cargando.")
        self.marchaAtras = True

    def getAtributos(self):
        super().getAtributos()
        print("Carga :", str(self.carga))

    def getAcciones(self):
        super().getAcciones()
        print("El vehículo está siendo cargado: " + str(self.cargar))

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, ancho, alto, marchas, asientos):
        super().__init__(color, ruedas, ancho, alto, marchas, asientos)

        self.saltar = False
        self.derrapar = False

    def Saltar(self):
        print("El vehículo está saltando.")
        self.saltar = True

    def Derrapar(self):
        print("El vehículo está derrapando.")
        self.derrapar = True

    def getAcciones(self):
        super().getAcciones()
        print("El vehículo está saltando: " + str(self.saltar))
        print("El vehículo está derrapando: " + str(self.derrapar))

class Moto(Coche, Bicicleta):
    def __init__(self, color, ruedas, ancho, alto, marchas, asientos, cilindrada, aireacondicionado):
        Coche.__init__(self, color, ruedas, ancho, alto, marchas, asientos, cilindrada, aireacondicionado)
        Bicicleta.__init__(self, color, ruedas, ancho, alto, marchas, asientos)

    def __str__(self):
        return f"{self}"

    def getAtributos(self):
        Bicicleta.getAtributos(self)
        print("Cilindrada :", str(self.cilindrada))

    def getAcciones(self):
        Bicicleta.getAcciones(self)
        print("El vehículo está arrancado: " + str(self.arrancar))

class Moto2(Coche, Bicicleta): #Solución propuesta
    def __init__(self, color, ruedas, ancho, alto, marchas, asientos, cilindrada):
        super().__init__(color, ruedas, ancho, alto, marchas, asientos, cilindrada, aireacondicionado=False) #Parece que "anula" uno de los parámetros que no nos sirven de una clase heredada con un booleano




print("---COCHE---")
citroenC3 = Coche("Rojo", 4, 130,170, 5, 5,1.4,"AA")
citroenC3.getAtributos()
citroenC3.getAcciones()

print("---FURGONETA---")
kangoo = Furgoneta("Azul", 4, 130, 210, 6, 8, 2.0, "Climatizador", 1000)
kangoo.MarchaAtras()
kangoo.getAtributos()
kangoo.getAcciones()

print("---BICICLETA---")
orbea = Bicicleta("Verde", 2, 30, 120, 21, 1,)
orbea.getAtributos()
orbea.Saltar()
orbea.getAcciones()


print("---MOTO---")
zip = Moto2("Azul", 4, 130, 210, 21, 1, 999)
zip.getAtributos()
zip.Saltar()
zip.Arrancar()
zip.MarchaAtras()
zip.getAcciones()
print(zip)


