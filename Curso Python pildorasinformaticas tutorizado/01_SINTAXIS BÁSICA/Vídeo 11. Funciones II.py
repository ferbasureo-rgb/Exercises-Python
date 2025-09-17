def imprimir():
    print("Voy a hacer una prueba para imprimir esto 15 veces.")
    print("A ver si sale bien.")
    print(f"Esta es la vez nº: {i+1}")

for i in range(15):
    imprimir()

def imprimeMensaje():
    return "Este es el mensaje"

x = imprimeMensaje() + "ahora mismo."
print(x)