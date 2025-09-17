trabajadores = [
                "Paula",
                "Jose",
                "Pedro",
                "Ana",
                "Sandra"
]

if "Pedros" in trabajadores:
    print("Se encuentra")
else:
    print("No se encuentra")

lenguajes_Trim1= "Java, Python, PHP, C#, HTML, JavaScript"
if "v" in lenguajes_Trim1:
    print("Se encuentra este lenguaje.")
else:
    print("No se encuentra este lenguaje")

if "CSS" not in lenguajes_Trim1:
    print("No se encuentra este lenguaje.")
else:
    print("Se encuentra este lenguaje")

#Se puede cambiar la posición del not

if not "CSS" in lenguajes_Trim1:
    print("No se encuentra este lenguaje.")
else:
    print("Se encuentra este lenguaje")