# También se puede escribir un diccionario así: expendedora = dict(Agua50ml=1, Agua75ml=1.50, CocaCola=2.5, Fanta=2.5)
expendedora = {
    "Agua 50ml": [1,1],
    "Agua 75ml": [2,1.50],
    "Coca Cola": [3,3.50],
    "Fanta": [4,3]
}
# Elabora un listín de precios visible al usuario.
print("""--- LISTA DE PRECIOS --- """)
"""for k,v in expendedora.items():
    print(v[0], k.upper()+": ", float(v[1])," €")""" # Lo hice así antes

for k in expendedora:
    v = expendedora[k]
    print(v[0], k.upper()+": ", float(valor[1]), " €")

# Función para realizar la compra del producto
def buy():
    # Creo una lista vacía
    numeros = []
    # En la lista números, añado los códigos de producto presentes en el índice 0 de los valores
    for i,j in list(expendedora.values()):
        numeros.append(i)
    n_articulo = int(input("Inserte código de artículo: "))
    # Creo un bucle para comprobar si el código del artículo está dentro del rango proporcionado: si no está, tengo que volver a introducir un código válido.
    while n_articulo not in numeros:
        n_articulo = int(input("Inserte código correcto, no hay en stock: "))
    # Si el código corresponde a un producto en stock continúa la función.
    else:
        for k,v in expendedora.items():
            #Creo un bucle que recorra todos los items del diccionario hasta que el número introducido coincida con el valor del código de producto
            if n_articulo == v[0]:
                print(f"Ha elegido {k}: Inserte {v[1]:.2f} euro(s).")
                cash = float(input("Inserte dinero: "))
                # Si el dinero introducido es menor que el valor del producto, un bucle me obliga a seguir introduciendo monedas.
                while cash < v[1]:
                #La moneda que introduzco se suma al cash que ya había en la máquina.
                    cash = cash + float(input(f"Ha introducido {cash:.2f} euro(s). Introduzca la cantidad correcta: "))
                else:
                #Cuando el cash coincide con el precio del producto, va expedido en la bandeja.
                    print("Expedido su producto, recójalo de la bandeja. Gracias por su compra.")
                if cash > v[1]:
                #La máquina arroja el resto si introduje más dinero del necesario.
                    print(f"Recoja el resto: {cash-v[1]:.2f}")
buy()


