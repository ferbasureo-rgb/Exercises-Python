import requests
from bs4 import BeautifulSoup

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text,'html.parser')

iconos = docFinal.select(".emoji") #Devuelve una lista

print(iconos[0].text)

titulos = docFinal.find_all('a')
for parrafo in titulos:
    print(parrafo.text)

for parrafo in titulos:
    print(parrafo.attrs)

#for parrafo in docFinal.find_all('p'):

    #print(parrafo.attrs)
    #print(parrafo.text)