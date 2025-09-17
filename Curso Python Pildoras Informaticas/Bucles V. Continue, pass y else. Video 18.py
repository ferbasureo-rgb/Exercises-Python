for letra in "Python":

    if letra == "h":
        continue

    print("Viendo la letra: " + letra)


nombre = "Pildoras Informaticas"

contador=0

for i in nombre:
    if i == " ":
        continue
    contador+=1 # Operativa para ignorar el espacio en los caracteres

print(contador)

"""Pass"""

class miClase:
    pass # Para implementar más tarde, devuelve valor nulo

email = input("Introduce email: ")

lista = []
for i in email:
    lista.append(i)
    if i == "@":
        arroba=True
        break

else:
    arroba=False

print(arroba)
print(lista)
fer


