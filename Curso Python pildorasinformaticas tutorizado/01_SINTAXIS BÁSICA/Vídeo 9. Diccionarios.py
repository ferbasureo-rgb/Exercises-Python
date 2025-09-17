paises = "España", "Reino Unido", "Francia", "Colombia"

lasCapitales = "Madrid", "Londres", "París", "Bogotá"

print(paises, lasCapitales)

paisCapital = {}
x = 0
for pais in paises:
    paisCapital[pais] = lasCapitales[x]
    x += 1

paisCapital["Italia"]="Roma"


paisCapital["Reino Unido"]="Brighton"

del paisCapital["Reino Unido"]

print(paisCapital)

datos ={"España": "Madrid",
        23: "M Jordan",
        "Mosqueteros": 3,
        "Earth": True
}
print(datos)

claveCapitales=["España", "Reino Unido", "Colombia", "Portugal"]

capitalesMundo={claveCapitales[0]: "Madrid",
                claveCapitales[1]: "Londres",
                claveCapitales[2]: "Bogotá",
                claveCapitales[3]: "Lisboa"}

print(capitalesMundo)

print(capitalesMundo["Colombia"])

print(capitalesMundo.keys())
print(capitalesMundo.values())
print(len(capitalesMundo))

datosJordan = {
    23: "M Jordan",
    "Nombre": "Michael",
    "Equipo": "Chicago Bulls",
    "Squadra": "Chicago Bulls",
    "Anillos": [1991,1992,1993,1996,1997,1998]
}
print(datosJordan["Anillos"])

print(datosJordan.items())
for item in datosJordan.items():
    print(item)
    print(type(item))
lista = []
for k, v in datosJordan.items():
    if "Chicago Bulls" in v:
        lista.append(k)
print(lista)

lista = [k for k, v in datosJordan.items() if "Chicago Bulls" in v]
print(lista)

edades = dict(María=23, José=38)
edades["Hijos"]=dict(Juan=1, Guille=2)
print(edades["Hijos"]["Juan"])
