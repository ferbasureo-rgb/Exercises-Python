for i in ["Pildoras", "Informaticas", 2025]:
    print(i, end=", ")

email=False
arroba = False
punto = False
miEmail=input("Introduce tu email: ")
for i in miEmail:
    if i=="@":
        arroba =True
for i in miEmail:
    if i==".":
        punto = True

if arroba and punto == True:
    email = True

if email==True:
    print("Email es correcto.")
else:
    print("Email no es correcto.")

contador = 0
miEmail=input("Introduce tu email: ")
for i in miEmail:
    if i=="@" or i==".":
        contador += 1
if contador == 2:
    print("Email correcto!")
else:
    print("Email no es correcto!")