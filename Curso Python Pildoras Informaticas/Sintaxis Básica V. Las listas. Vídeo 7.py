nombreLista = ["elem1", "elem2", "elem3"]

def funcion(numero):
    lista=[]
    for i in range(numero+1):
        lista.append(i)
    return lista

print(funcion(10))

miLista2 = list(range(1,6))

miLista=["Maria", 53 , "Paco", True]
print(miLista[0])
miLista.append("Johnny") #añadir un elemento al final
miLista.insert(0,"Paolo") #insertar un elemento en un índice
miLista.extend(["Mamanico", "Cabesa"]) #añadir elementos
miLista.remove("Cabesa") #borrar este elemento
miLista.pop() #borrar último elemento
print(miLista)
print(miLista.count("Paolo"),"vez es la que aparece")
print(len(miLista), "nº de elementos") #
print(miLista.index("Paco")) #buscar en qué índice i se encuentra un elemento (si hay varios el primero)
print("Paco" in miLista)

miLista3 = miLista+miLista2
print(miLista3)



