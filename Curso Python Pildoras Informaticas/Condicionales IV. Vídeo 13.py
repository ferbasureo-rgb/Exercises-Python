print("---PROGRAMA DE BECAS 2026---")
try:
    distancia=int(input("Introduce la distancia a la que vive el alumno en km: "))
    print(distancia)

    hermanos=int(input("Introduce el número de hermanos del alumno: "))
    print(hermanos)

    salario = int(input("Introduce el rédito anual bruto en euros: "))
    print(salario)

    if distancia > 40 and hermanos > 2 or salario <= 20000:
        print("El alumno tiene beca")
    else:
        print("El alumno no tiene derecho a beca")
except:
    print("Introduzca sólo un valor numérico (sin unidades)")

print("--- INGENIERÍA OPTATIVAS ---")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

asignatura=input("Escribe la asignatura escogida: ")
opcion = asignatura.lower()

if opcion in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura elegida no es compatible.")







