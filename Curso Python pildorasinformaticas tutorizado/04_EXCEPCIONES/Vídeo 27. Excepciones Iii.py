def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print("El resultado es: " + str(op1 / op2))
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
    except ValueError:
        print("Introduzca un número válido.")
    finally:
        print("Se ha intentado ejecutar la función en su totalidad.")

divide()
print("Cálculo finalizado. Continuamos con el programa.")

def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print("El resultado es: " + str(op1 / op2))

    finally: #Podemos tener un finally con try sólo, para intentar lo anterior y aunque dé un error, se ejecute el finally(suele ser útil para romper conexiones con BBDD, etc.).
        print("Se ha intentado ejecutar la función en su totalidad.")

divide()
print("Cálculo finalizado. Continuamos con el programa.")