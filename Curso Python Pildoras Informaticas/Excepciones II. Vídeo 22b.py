def divide():
    try:
        op1 = float(input("Ingresa un numero: "))
        op2 = float(input("Ingresa otro numero: "))

        print("La división es: ", op1/op2)

    except ValueError:
        print("El numero ingresado no es valido.")

    except ZeroDivisionError:
        print("No se puede dividir entre 0.")

    finally: # Lo que haya en el finally, se ejecuta sí o sí, aunque salten excepciones y se pare el programa.
        print("Cálculo finalizado.")

divide()