def capitales_mundo(*ciudades): #con el asterisco, pide un nº indeterminado de elementos en formato tupla
    for capital in ciudades:
        for chr in capital:
            yield chr

capitales_devueltas=capitales_mundo("Berlín", "Hanoi", "Bogotá", "París", "Pekín")
print(next(capitales_devueltas))
print(next(capitales_devueltas))
print(next(capitales_devueltas))

def capitales_mundo2(*ciudades): #con el asterisco, pide un nº indeterminado de elementos en formato tupla
    for capital in ciudades:
        yield from capital

capitales_devueltas2=capitales_mundo2("Berlín", "Hanoi", "Bogotá", "París", "Pekín")
print(next(capitales_devueltas2))
print(next(capitales_devueltas2))
print(next(capitales_devueltas2))