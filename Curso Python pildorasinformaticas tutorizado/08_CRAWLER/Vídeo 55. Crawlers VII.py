from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time

class PostCrawled():

    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen

class PostExtractor():

    def extraeInfo(self):
        urlBase= "http://python.beispiel.programmierenlernen.io/index.php"

        posts = []
        while urlBase != "":

            miDoc = requests.get(urlBase)
            docFinal = BeautifulSoup(miDoc.text, 'html.parser')
            time.sleep(2)

            for card in docFinal.select(".card"):
                titulo = card.select(".card-title span")[1].text
                emoticono = card.select_one(".emoji").text #Select_one sólo accede a la primera clase que encuentre con ese valor introducido
                contenido = card.select_one(".card-text").text
                imagen = urljoin(urlBase, card.select_one("img").attrs["src"])

                crawled = PostCrawled(titulo, emoticono, contenido, imagen)
                posts.append(crawled)

            boton_siguiente = docFinal.select_one(".navigation .btn")
            if boton_siguiente:
                rutas_absolutas = urljoin(urlBase, boton_siguiente.attrs["href"])
                urlBase = rutas_absolutas
                print(rutas_absolutas)

            else:
                urlBase = ""

        return posts

unPost = PostExtractor()

listaPosts = unPost.extraeInfo()
print(listaPosts[1].titulo)
print(listaPosts[1].emoticono)
print(listaPosts[1].contenido)
print(listaPosts[1].imagen)

print("---")
for pst in listaPosts:
    print(pst.emoticono)
    print(pst.titulo)
    print(pst.contenido)
    print(pst.imagen)
    print()



