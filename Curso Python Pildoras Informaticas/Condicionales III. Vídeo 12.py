edad="hola"

try:
    if edad<100:
        print("Edad es correcta")
    else:
        print("Edad incorrecta")
except:
    print("El valor introducido es incorrecto.")

salario_presidente = int(input("Introduzca el salario presidente: "))
print("Salarios presidente: " + str(salario_presidente))

salario_director = int(input("Introduzca el salario director: "))
print("Salarios director: " + str(salario_director))

salario_jefe_area = int(input("Introduzca el salario jefe área: "))
print("Salarios jefe área: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduzca el salario administrativo: "))
print("Salarios administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("El salario es correcto")
else:
    print("Algo falla en esta empresa.")