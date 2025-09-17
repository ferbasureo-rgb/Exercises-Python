lista = list(range(1,16))
tupla = tuple(lista)
print(lista, tupla)

print(tupla.index(3))

tupla2 = "a", "b", "c", "d"
tupla2_lista = list(tupla2)
print(tupla2_lista)

misDatos = tupla2_lista + lista
misDatos=tuple(misDatos)

misDatosLista=list(misDatos)
print(misDatosLista)

print(misDatos)

print("El índice 15 contiene el siguiente número:",misDatos[15])
print(233 in misDatos)
try:
    print(misDatos.index(233))
except ValueError:
    print("El objeto no está en la tupla. ")

print("El programa continúa.")

misDatos=["Juan", 13, 1, 2002]

misDatosTupla=tuple(misDatos)

print(misDatosTupla)
print(misDatosTupla.count("Juan"))

print(len(misDatosTupla))

#Desempaquetado de tupla/lista: IMPORTANTE ESTO ----------------->>>>>>>>>>>
misDatosLista = tuple(misDatos)

nombre, día, mes, año = misDatosTupla
a = list(misDatosTupla)
print(a)
nombre2, dia2, mes2, año2 = a
print(nombre)
print(nombre2)

print(dia2, día)

data= 1,2,3,4,5
data = list(data)
print(data)