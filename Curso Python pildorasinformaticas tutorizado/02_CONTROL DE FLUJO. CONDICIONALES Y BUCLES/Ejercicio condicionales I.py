"""
EJERCICIO CONDICIONALES. TIPO IMPOSITIVO DE LA DECLARACIÓN DE LA RENTA.

Los tramos impositivos de un país en concreto son los que figuran en la siguiente tabla:

Renta:          Tipo impositivo:
Hasta 12000 €           7%
Entre 12000€ y 18000€   15%
Entre 18000€ y 35000€   21%
Entre 35000 y 70000€    35%
Más de 70000€           45%

Crea un programa que pregunte por consola la renta. En función de la renta introducida, el programa devolverá el texto: “A la renta (aquí iría la renta introducida) le corresponde un (aquí iría el tipo impositivo) de tipo impositivo.

Ejemplo: En caso de introducir por consola 13500, el programa devolverá el texto: “A la renta 13500 le corresponde un 15% de tipo impositivo”

El programa debe permitir la introducción de rentas decimales.
"""


ingresos = float(input("Introduzca la renta anual: "))


def renta(ingresos):
    coeficiente = ""
    while ingresos < 0:
        print("La renta introducida es negativa.")
        ingresos = float(input("Introduzca la renta anual: "))
    else:
        if ingresos < 12000:
            coeficiente = "7%"
        elif ingresos < 18000:
            coeficiente = "15%"
        elif ingresos < 35000:
            coeficiente = "21%"
        elif ingresos < 70000:
            coeficiente = "35%"
        else:
            coeficiente ="45%"
        return print(f"A la renta {ingresos} le corresponde un {coeficiente} de tipo impositivo.")


renta(ingresos)

