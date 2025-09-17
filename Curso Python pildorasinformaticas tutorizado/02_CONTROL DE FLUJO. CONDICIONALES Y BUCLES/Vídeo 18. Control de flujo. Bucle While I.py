contador = 1
numero = int(input("Introduce número: "))
while contador < 3 and numero < 0:
   contador += 1
   numero = int(input("Introduce número: "))

print("Bucle pasado.")