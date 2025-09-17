nombre = "Fernando Rodríguez"
contador_caracteres = 0

for i in nombre:
    if i==" ":
        continue
    contador_caracteres += 1

print(contador_caracteres)


for i in nombre:
    pass

class EjemploClase:
    pass

email =input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba=True
        break

else:
    arroba=False

print(arroba)
