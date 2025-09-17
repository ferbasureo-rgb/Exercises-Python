class Coche():

    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if self.__enmarcha:
            return "El coche está en marcha."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene", self.__ruedas, " ruedas; un ancho de ",self.__anchoChasis, " y un largo de ", self.__largoChasis)

miCoche01=Coche()

print(miCoche01.arrancar(True)) #Arrancamos el coche:

miCoche01.estado()

print("------A continuación creamos el segundo objeto------")

miCoche02=Coche()


print(miCoche02.arrancar(False))
miCoche02.estado()

miCoche02.largoChasis=500

miCoche02.estado()

print(miCoche02._Coche__ruedas, 25)

print(miCoche02.largoChasis)

print(miCoche02._Coche__ruedas)