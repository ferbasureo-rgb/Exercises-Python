class Coche():

    def __init__(self, nombre="Coche"):
        self.nombre = nombre
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def __str__(self):
        return self.nombre

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos

        if self.__enmarcha:
            chequeo=self.__chequeo_interno()

        if self.__enmarcha and chequeo:
            return f"El {self} está en marcha."
        elif self.__enmarcha and chequeo==False:
            return "Algo ha ido mal en el chequeo, no se puede arrancar."
        else:
            return f"El {self} está parado."

    def estado(self):
        print(f"El {self} tiene", self.__ruedas, " ruedas; un ancho de ",self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno.")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina == "ok" and  self.aceite == "ok" and self.puertas=="cerradas":
            return True
        else:
            return False


miCoche01=Coche("Coche01")

print(miCoche01.arrancar(True)) #Arrancamos el coche:
miCoche01.estado()
miCoche01._Coche__chequeo_interno() #Así sí podríamos forzar la entrada al método encapsulado.

print("""
------A continuación creamos el segundo objeto------
""")

miCoche02=Coche("Coche02")
print(miCoche02.arrancar(False))
miCoche02.estado()
miCoche02._Coche__chequeo_interno()#Así sí podríamos forzar la entrada al método encapsulado.