#No permiten añadir, eliminar, mover elementos (no append, extend, remove)

tupla = "1","2","3","4"

print(tupla)

miTupla = ("Juan", 13, 1, 1995)
print(miTupla.index(13)) #Se puede, antes no
print("Juan" in miTupla)

miLista=list(miTupla)
miLista2 = miLista.copy()
miLista2.append("Willy") #añadir elementos
miTupla2=tuple(miLista) #convertir lista en tupla

print(miTupla2.count("Willy")) #contar cuántas veces está en la tupla (también vale para listas)
print(len(miTupla2), "nº de elementos") #nº de elementos

print(miLista2)
print(miTupla2)

miTupla3 = "Jimmy", 15, 35, 1987 #empaquetado de tupla
print(miTupla3)

name, day, month, year = miTupla3 #Con esto asigno cada uno de los valores a las variables declaradas
print(name, day, month, year)

address, city, state, zip = "alameda", "malaga", "spain", 29009 #Asigno valores a claves
print(address)
"miTupla3.append("Architect")" #no se pueden añadir elementos a una tupla