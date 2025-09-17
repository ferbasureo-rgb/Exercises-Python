#Buscar en la documentación de python "Built-in functions"

a = "5"
a_int = int(a)
print(type(a_int))

a_float = float(a)
print(type(a_float))

f = "Mi nombre es Fernando y soy Arquitecto, estoy aprendiendo a programar."
lista = f.split(" ")
print(lista)

empleados = ["Ana",
             "Juan",
             "Jose",
             "Pedro",
             "Maria",
             "Alabama",
             "Arizona",
             "Arlinda",
             "California",
             "Colorado"
             ]
empleados.insert(-1,"y")
empleados.append(".")
print(empleados)
texto_join = " ".join(empleados) #Le estoy diciendo a P que componga un texto con los argumentos de la lista separados por un espacio " ".
print(texto_join)






