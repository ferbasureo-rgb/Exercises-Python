x,y = 10, 20

print(f"La suma de {x} y {y} es {x+y}.")

import timeit

nombre = "Juan"
edad = 30

# Usando f-strings
calculo_f_string = timeit.timeit('f"Hola {nombre} tienes {edad} años."', globals=globals(), number=1000000)

# Usando .format()
calculo_format = timeit.timeit('"Hola {} tienes {} años."'.format(nombre, edad), globals=globals(), number=1000000)

print(f"Tiempo usado f-strings: {calculo_f_string} segundos.")
print(f"Tiempo usado .format: {calculo_format} segundos.")

pi = 3.14159
print(f"El valor de pi {pi:.2f}")

print("El valor de pi es {:.2f}".format(pi))

