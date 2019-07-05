from urllib import request
from urllib.request import urlopen, re
from bs4 import BeautifulSoup

def conseguirTitulos(x):
    titulos = soup.find_all(True, {'class': ['info']})

    for i in titulos:
        # print (i.contents)
        title_tag = i.contents[3]
        print(title_tag.string)
        texto=(title_tag.string).__str__
        x.write(texto)



def conseguirLinks():
    for i in linkFoto:
        # print (i.contents)
        link = i.find('a')
        modificarCadena(link)
        #print(link)

def modificarCadena(cadena):
    #cadena=cadena.__str__
    for i in cadena:
        if(i>=4):
            if(i+(i-1)+(i-2)+(i-3)=="ferh"):
                x=i
                while(x != '"'):
                    contador=contador+1
                    string=string+x
                    i=i+1
                    x=i
                print(string)
def crearArchivo(nombre):
    x=open(nombre+".txt","w")

def cerrarArchivo(x):
    x.close()

conexion=urlopen("https://listas.20minutos.es/lista/100-animes-mas-populares-y-mejores-de-la-historia-354787/")
html= conexion.read()
soup = BeautifulSoup(html,"html.parser")
x=open("titulos.txt","w")
conseguirTitulos(x)
x.close()

linkFoto = soup.find_all('div',{'class': ['elemento']})

for i in linkFoto:
    #print (i.contents)
    link=i.find('a')
    #modificarCadena(link)


''''
re=request.urlopen("https://listas.20minutos.es/lista/100-animes-mas-populares-y-mejores-de-la-historia-354787/")
    #get("https://listas.20minutos.es/lista/100-animes-mas-populares-y-mejores-de-la-historia-354787/")



filtrado = BeautifulSoup(html)

for link in filtrado.find_all(True,{'class':['listas_elementos']}):
    print(link.get('href'))'''