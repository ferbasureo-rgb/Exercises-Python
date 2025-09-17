a = list()
for i in range(10):
    a.append(i)

print(a)

trabajadores = ["Ana", "Antonio", "María", "Pedro", "Laura"]

print(trabajadores[2:1])

edad = [1, 2, 3, 4, 5]
print(trabajadores + edad)

trabajadores.append(edad)
print(trabajadores)

del trabajadores[-1]
print(trabajadores)

trabajadores.remove("Antonio")
print(trabajadores)

print(trabajadores.index("Pedro"))

print(trabajadores.count("Laura"))

trabajadores.insert(1, "Antonio")
print(trabajadores)

print("---QUIZ---")
print(trabajadores.index("Pedro"))

trabajadores.extend("Murcia" "Willy")
print(trabajadores)