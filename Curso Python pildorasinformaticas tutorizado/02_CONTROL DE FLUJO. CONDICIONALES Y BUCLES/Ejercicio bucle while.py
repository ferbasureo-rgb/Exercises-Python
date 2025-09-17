import random

randomNum = random.randint(1,100)


def ruleta(max_intentos):
    userNum = int(input("Introduce un numero del 1 al 100: "))
    n_intentos = 1
    while userNum != randomNum:
        if userNum > randomNum:
            print("El núnero aleatorio es menor que {}.".format(userNum))
        else:
            print("El número aleatorio es mayor que {}.".format(userNum))
        n_intentos += 1
        userNum = int(input("Introduce un numero: "))
        if n_intentos == max_intentos:
            print("HAS FALLADO... Se ha superado el número de intentos.")
            break
    else:
        print(f"¡CORRECTO! Has utilizado {n_intentos} intento(s).")

ruleta(5)
