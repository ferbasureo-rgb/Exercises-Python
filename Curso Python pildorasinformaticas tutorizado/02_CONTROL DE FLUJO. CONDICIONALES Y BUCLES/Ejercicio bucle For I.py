"Crea una función que reciba dos listas por parámetros. La función debe comparar ambas listas, devolviendo True si las listas son idénticas y False si no lo son."

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9,10]
z = x


def comparar(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    for i in range(len(lista1)):
        print(lista1[i], lista2[i])
        if lista1[i] != lista2[i]:
            return False
    return True
