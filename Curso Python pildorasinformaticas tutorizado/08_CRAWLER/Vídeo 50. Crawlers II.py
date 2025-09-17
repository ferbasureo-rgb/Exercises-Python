import requests
from bs4 import BeautifulSoup

miReq = requests.get('https://www.muchodeporte.com')
print(miReq.status_code)

print(miReq.headers)
miDoc = miReq.text

"""

    <html>
        <body>
            
            <p>Este es el primer párrafo</p>
            
            <p>Este es el segundo párrafo</p>
                       
            <a>Es un vínculo</a>
            
        </body>
    
    </html>"""

docFinal=BeautifulSoup(miDoc,"html.parser")
for parrafo in docFinal.find_all('a'):
    print(parrafo.text)

print(docFinal)
print(docFinal.find_all('p'))

