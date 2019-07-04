from urllib.request import urlopen
from bs4 import BeautifulSoup

def conseguirTitulos():
    titulos = soup.find_all(True, {'class': ['info']})
    for i in titulos:
        # print (i.contents)
        title_tag = i.contents[3]
        print(title_tag.string)


conexion=urlopen("https://listas.20minutos.es/lista/100-animes-mas-populares-y-mejores-de-la-historia-354787/")
html= conexion.read()
soup = BeautifulSoup(html)

linkFoto = soup.find_all(True, {'class':['fotolista']})

for i in linkFoto:
    #print (i.contents)
    title_tag = i.contents[2]
    print(title_tag.string)
