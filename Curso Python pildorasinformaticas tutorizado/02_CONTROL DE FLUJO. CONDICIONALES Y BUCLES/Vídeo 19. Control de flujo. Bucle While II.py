edad = int(input("Introduce edad: "))

while edad<0 or edad>100:
    if edad<0:
        print("Has introducido una edad negativa.")
    else:
        print("has introducido una edad demasiado alta.")
    edad = int(input("Introduce edad: "))
    break

print("Gracias, puedes pasar.")
print("Edad del usuario", edad)

print("Este programa halla la raíz cuadrada de un valor numérico.")

import math

numero = int(input("Introduce número: "))

n_intentos = 1
while numero<0:
    print("Valor numérico no puede ser negativo.")
    numero = int(input("Introduce número: "))
    n_intentos += 1
    if n_intentos > 3:
        print("Consumido límite de intentos.")
        break
num = float(numero)
if n_intentos > 3:
    print("no puedo realizar el cálculo")
else:
    x = float(math.isqrt(numero))
    print(x)
