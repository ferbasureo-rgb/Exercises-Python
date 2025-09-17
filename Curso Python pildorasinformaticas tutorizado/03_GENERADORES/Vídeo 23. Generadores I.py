def sonPrimos(num1,num2):
    lista = []
    for num in range(num1, num2):
        if num < 2:
            continue
        es_primo = True
        for p in range(2, num):
            if num%p == 0:
                es_primo = False
                 #Opcional, para que no haga más comprobaciones innecesarias
        if es_primo:
            lista.append(num)
    return lista

def generadorPrimos(num1, num2):
    for primo in sonPrimos(num1, num2):
        yield primo

genPrimos = generadorPrimos(0,15)
print("probando generador")
print(next(genPrimos))
print(next(genPrimos))
print(next(genPrimos))
print(next(genPrimos))
print(next(genPrimos))
print("fin de pruebas")

"NUMEROS PARES"

def numeros_pares(limite):
    num=1
    while num < limite:
        yield num*2
        num+=1

sucesionPares = numeros_pares(10)
print(next(sucesionPares))
print(next(sucesionPares))
print("Ahora voy a ejecutar el resto por bucle: ")
for i in sucesionPares:
    print(i)

