def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operación fallida."

limite = 3
intentos=0
while True:
    try:
        op1 = int(input("Introduce el primer número: "))
        op2 = int(input("Introduce el segundo número: "))
        break
    except ValueError:
        print("Introduzca un valor numérico.")
        intentos=intentos+1
        if intentos==limite:
            print("Ha superado el número de intentos.")
            exit()

operacion = input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))


elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada.")

print("Operación ejecutada. Continuación de ejecución del programa.")