capitales = dict(China="Pekín", India="Nueva Delhi", Indonesia="Yakarta", Japón="Tokio", Bangladesh="Dacca")

#Recorre las claves
for clave in capitales:
    print(clave)
for clave in capitales.keys():
    print(clave)

#Recorrer los valores
for clave in capitales:
    valor = capitales[clave]
    print(clave)
    print(valor)

print(capitales.items())

#Recorrer items
for clave, valor in capitales.items():
    print(clave + "->" + valor)


clave = capitales.setdefault("España", "Madrid")
print(clave)
print(capitales)
capitales.setdefault("España", "Barcelona")
print(capitales)


