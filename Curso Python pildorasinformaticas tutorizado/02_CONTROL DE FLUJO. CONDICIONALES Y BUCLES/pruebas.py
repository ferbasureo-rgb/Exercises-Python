miDiccionario= {"España":"Madrid",
                "Colombia":"Bogotá",
                "USA":"Washington"
                }

valor=miDiccionario.setdefault("Francia","Paris")
print(valor)
print(miDiccionario)
miDiccionario.set