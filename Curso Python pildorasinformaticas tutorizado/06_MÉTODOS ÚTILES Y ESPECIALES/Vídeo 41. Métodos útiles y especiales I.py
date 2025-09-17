# En la documentación de python lo llama "Método de las cadenas"

string = "Esta oración está hecha para probar el método de las cadenas y las " +str(1324) +" maneras que hay de operar con ellos."
print(string)
nUsuario = input("Ingresa tu usuario: ")


print("El usuario introducido es: ", nUsuario.upper())
print("El usuario introducido es: ", nUsuario.lower())
print("El usuario introducido es: ", nUsuario.capitalize())

edad=input("Introduce tu edad, por favor: ")
while edad.isdigit()==False:
    print("Valor introducido no numérico.")
    edad=input("Vuelve a introducir tu edad, por favor: ")

if (int(edad)<18):
    print("No puedes pasar.")

else:
    print("Puedes pasar.")