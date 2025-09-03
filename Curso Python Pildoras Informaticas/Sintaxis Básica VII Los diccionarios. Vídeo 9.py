#Diccionarios
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(len(abecedario))
dict = {}
for i in range(len(abecedario)):
    dict[abecedario[i]] = i+1
print(dict)

print(dict.keys())
print(dict.values())
print(dict.items())

mydict = {"Alemania": "Berlin",
          "Francia": "Paris",
          "España": "Madrid",
          "Reino Unido": "Londres"
          }
print(mydict["Alemania"]) # Me revela el valor de la clave dada

mydict["Italia"]="Lisboa" #Añadir un elemento
print(mydict)
mydict["Italia"]="Roma" #Se puede corregir
print(mydict)
mydict.pop("Italia") #Se elimina el elemento dado, sin darlo da error, no como en las listas, que no se da y elimina el último
print(mydict)
mydict.popitem() #Se borra el último
print(mydict)
mydict["Holanda"]=None
print(mydict)
del mydict["Holanda"]
mydict.pop("Afganistan", None) #Con valor por defecto no lanza error, del sí, si no existe la clave
print(mydict)

myList = list(mydict.keys()) #Lista con claves del diccionario
myList = list(mydict.values())  #lista con los valores

print("---")

miTupla=("Spain", "France", "UK", "Germany")
countries = {miTupla[0]:"Madrid",
             miTupla[1]:"Paris",
             miTupla[2]:"London",
             miTupla[3]:"Berlin"}

print(countries["France"])

dicciotupla = {"Jordan": 23,
               "Team": "Chicago",
               "Nombre": "Michael",
               "Anillos":(1990, 1992,1993, 1995)}

print(dicciotupla["Team"])

dicciodoble = {"Jordan": 23,
               "Team": "Chicago",
               "Nombre": "Michael",
               "Anillos": {"Temporadas":(1990, 1992,1993, 1995)}
               }
print(dicciodoble["Anillos"]["Temporadas"])
print(dicciodoble.keys()) #Enumera keys
print(dicciodoble.values()) #Enumera values
print(len(dicciodoble))
print(dicciodoble.items()) #Agrupación Key+Value
#Buscar una clave que pertenezca a un valor recorriendo los items.
def find_value():
    for key, value in dicciodoble.items():
        if value == "Michael":
            print(key)
find_value()
# Buscar keys que correspodan a values con list comprehension (lista)
finding_value = [key for key,value in dicciodoble.items() if value == "Michael" or value == "Chicago"]
print(finding_value)
