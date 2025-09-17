class CuentaCorriente():

    def __init__(self, titular):
        self.titular=titular
        self.IBAN="ES68 4769 50 4578756 1527 1540"
        self.saldo=0 #con una _, heredable pero no editable / con dos __, no editable ni heredable
    def getDatos(self):
        print("IBAN: "+self.IBAN)
        print("Titular: "+self.titular)
        print("Saldo: " + str(self.saldo))

    def ingresar(self,ingreso):
        self.saldo = self.saldo + ingreso
        print("Ha ingresado "+str(ingreso)+" euros.")
    def retirar(self,retirar):
        if retirar <= self.saldo:
            self.saldo = self.saldo - retirar
            print("Ha retirado "+str(retirar)+" euros.")
        else:
            print("No dispone de saldo suficiente.")

class CuentaJoven(CuentaCorriente):

    def __init__(self, titular):
        super().__init__(titular)
        self.bonus = False

    def getBonus(self):
        self.saldo = self.saldo + 375
        self.bonus = True
        print("Su bonus de bienvenida ha sido activado.")

    def ingresar(self, ingresando):
        super().ingresar(ingresando)

    def retirar(self, retirando):
        super().retirar(retirando)

    def getDatos(self):
        super().getDatos()
        if self.bonus:
            estadoBonus = "Activado"
        else:
            estadoBonus = "No activado"
        print("Bonus: " + estadoBonus)




miCuentaJoven = CuentaJoven("José Díaz Romero")
miCuentaJoven.getDatos()
miCuentaJoven.getBonus()
miCuentaJoven.getDatos()
miCuentaJoven.ingresar(5000)
miCuentaJoven.getDatos()
miCuentaJoven.retirar(6000)
miCuentaJoven.getDatos()
miCuentaJoven.retirar(5230.56)
miCuentaJoven.getDatos()