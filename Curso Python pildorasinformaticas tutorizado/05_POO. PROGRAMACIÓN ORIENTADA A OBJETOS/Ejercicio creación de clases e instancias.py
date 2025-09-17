class CuentaCorriente():

    def __init__(self, titular):
        self.titular=titular
        self.IBAN="ES68 4769"
        self.__saldo=0
    def getter(self):
        print("IBAN: "+self.IBAN)
        print("Titular: "+self.titular)
        print("Saldo: " + str(self.__saldo))

    def ingresar(self,ingreso):
        self.__saldo = self.__saldo + ingreso
        print("Ha ingresado "+str(ingreso)+" euros.")
    def retirar(self,retirar):
        if retirar <= self.__saldo:
            self.__saldo = self.__saldo - retirar
            print("Ha retirado "+str(retirar)+" euros.")
        else:
            print("No dispone de saldo suficiente.")
miCuenta=CuentaCorriente("Juan Jiménez Jaramillo")

miCuenta.ingresar(5000)
miCuenta.ingresar(4000)
miCuenta.retirar(8500)
miCuenta.getter()
miCuenta.retirar(400)
miCuenta.getter()
miCuenta.__saldo=500000
miCuenta.getter()