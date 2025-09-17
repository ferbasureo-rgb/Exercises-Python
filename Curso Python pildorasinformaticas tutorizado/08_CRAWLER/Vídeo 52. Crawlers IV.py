import requests
from bs4 import BeautifulSoup

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text,'html.parser')

for cuerpoTexto in docFinal.select(".card-text"):
    print(cuerpoTexto.text)
    print(" ")

for imagen in docFinal.select(".card-block img"):
    print(imagen.attrs['src'])
    print(" ")

