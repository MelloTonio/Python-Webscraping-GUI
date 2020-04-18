from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import requests #pip install requests
from bs4 import BeautifulSoup
import time
from datetime import datetime



weather_NY = 'https://weather.com/weather/today/l/f892433d7660da170347398eb8e3d722d8d362fe7dd15af16ce88324e1b96e70'
searching_6 = requests.get(weather_NY)
soup = BeautifulSoup(searching_6.text,'html.parser')
cidade_NY = soup.find(class_='h4 today_nowcard-location')
temperatura_NYf = soup.find(class_='today_nowcard-temp') 
temperatura_NYf = temperatura_NYf.text.replace('°','')
temperatura_NYc = (((int(temperatura_NYf) - 32) * 5) / 9)
print('ok')
#################################################################
weather_London = 'https://weather.com/weather/today/l/UKXX0085:1:UK'
searching_5 = requests.get(weather_London)
soup = BeautifulSoup(searching_5.text,'html.parser')
cidade_LO = soup.find(class_='h4 today_nowcard-location')
temperatura_LOf = soup.find(class_='today_nowcard-temp') 
temperatura_LOf = temperatura_LOf.text.replace('°','')
temperatura_LOc = (((int(temperatura_LOf) - 32) * 5) / 9)
print('ok')
#################################################################
weather_MG = 'https://weather.com/pt-BR/clima/hoje/l/BRXX0131:1:BR'
searching_4 = requests.get(weather_MG)
soup = BeautifulSoup(searching_4.text,'html.parser')
cidade_MG = soup.find(class_='h4 today_nowcard-location')
temperatura_MG = soup.find(class_='today_nowcard-temp')
print('ok')
#################################################################
mg_News = 'https://g1.globo.com/mg/zona-da-mata/cidade/juiz-de-fora/'
searching_9 = requests.get(mg_News)
soup = BeautifulSoup(searching_9.text,'html.parser')
news_MG = soup.find('a',class_='feed-post-link gui-color-primary gui-color-hover')
news_MG_2 = soup.find_all('a',class_='feed-post-link gui-color-primary gui-color-hover')
print('ok')
#################################################################
ny_times = 'https://www.nytimes.com/'
searching_7 = requests.get(ny_times)
soup = BeautifulSoup(searching_7.text,'html.parser')
NY_NEWS = soup.find_all('div',class_='css-1ez5fsm esl82me1')
print('ok')
###################################################
london_news = 'https://www.bbc.com/news/england'
searching_8 = requests.get(london_news)
soup = BeautifulSoup(searching_8.text,'html.parser')
LONDON_NEWS = soup.find_all('a',class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')
#LONDON_NEWS_1 = soup.find('span',class_='nw-c-related-items__text gs-u-align-bottom')
#LONDON_NEWS_2 = soup.find('h3',class_='gs-c-promo-heading__title gel-paragon-bold gs-u-mt+ nw-o-link-split__text')
#LONDON_NEWS_3 = soup.find(class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')
###################################################
print('ok')
now = datetime.now()
weather = 'https://weather.com/pt-BR/clima/hoje/l/S%C3%A3o+Paulo+S%C3%A3o+Paulo?canonicalCityId=d7593e91d7e1447404d3a75fc1f7e0513bfcc5bdd74b81f6b4299f68b5689392'
searching_2 = requests.get(weather)
soup = BeautifulSoup(searching_2.text, 'html.parser')
cidade = soup.find(class_='h4 today_nowcard-location')
temperatura = soup.find(class_='today_nowcard-temp')
print('ok')
###################################################
uol = 'https://www.uol.com.br/'
searching = requests.get(uol)
soup = BeautifulSoup(searching.text, 'html.parser')
cabecalho_uol = soup.find(class_='chapeu color1')
noticia_UOL = soup.find('h1',class_='titulo color2')
noticia_UOL2 = soup.find('h2',class_='titulo color2')
print('ok')
####################################################
terra = 'https://www.terra.com.br/'
searching_3 = requests.get(terra)
t = BeautifulSoup(searching_3.text, 'html.parser')
noticiaTERRA = t.find('a',class_='main-url text')
print('ok')
###################################################
dolar = 'https://economia.uol.com.br/cotacoes/'
searching_10 = requests.get(dolar)
zzz = BeautifulSoup(searching_10.text,'html.parser')
cotacao_dolar = zzz.find_all('a',class_='subtituloGrafico subtituloGraficoValor')
print('ok')
###################################################
libra = 'https://www.beecambio.com.br/cotacao/libra-esterlina'
searching_11 = requests.get(libra)
searching0 = BeautifulSoup(searching_11.text,'html.parser')
cotacao_libra = searching0.find('span',class_='currencyValue')
print('ok')

def uol_not():
    web.label.setText('Principais Noticias - UOL')
    web.lineEdit.setText(cidade.text)
    web.lineEdit_2.setText(f'Temperatura: {temperatura.text}')
    web.lineEdit_3.setText(f'{cabecalho_uol.text}')
    web.lineEdit_4.setText(f'Noticia: {noticia_UOL.text}')
    web.lineEdit_6.setText(f'Noticia: {noticia_UOL2.text}')
    web.lineEdit_5.setText(f'Noticia: {noticiaTERRA.text}')
    web.lineEdit_7.setText(f'{now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}:{now.second}')
###################################################
    
x = 0
def trocar_cidade():
    global x
    sortear = [1,2,3,4]
    ra = sortear[0 + x]
    if ra == 1:
        web.label.setText('Principais Noticias - NY Times')
        web.lineEdit.setText(cidade_NY.text)
        web.lineEdit_3.setText(f'{NY_NEWS[0].text}')
        web.lineEdit_4.setText(f'Noticia: {NY_NEWS[1].text}')
        web.lineEdit_5.setText(f'Noticia: {NY_NEWS[2].text}')
        web.lineEdit_6.setText(f'Noticia: {NY_NEWS[3].text}')
        web.lineEdit_2.setText(f'Temperatura: {int(temperatura_NYc)} ºC')
        x += 1
    if ra == 2:
        web.label.setText('Principais Noticias - BBC London')
        web.lineEdit.setText(cidade_LO.text)
        web.lineEdit_3.setText(f'{LONDON_NEWS[0].text}')
        web.lineEdit_5.setText(f'Noticia: {LONDON_NEWS[1].text}')
        web.lineEdit_6.setText(f'Noticia: {LONDON_NEWS[2].text}')
        web.lineEdit_2.setText(f'Temperatura: {int(temperatura_LOc)} ºC')
        x += 1
    if ra == 3:
        web.label.setText('Principais Noticias - Juiz de Fora')
        web.lineEdit.setText(cidade_MG.text)
        web.lineEdit_3.setText(f'{news_MG.text}')
        web.lineEdit_4.setText(f'{news_MG_2[1].text}')
        web.lineEdit_5.setText(f'{news_MG_2[2].text}')
        web.lineEdit_6.setText(f'{news_MG_2[3].text}')
        web.lineEdit_2.setText(f'Temperatura: {temperatura_MG.text}')
        x += 1
    if ra == 4:
        web.label.setText('Principais Noticias - UOL')
        web.lineEdit.setText(cidade.text)
        web.lineEdit_2.setText(f'Temperatura: {temperatura.text}')
        web.lineEdit_3.setText(f'{cabecalho_uol.text}')
        web.lineEdit_4.setText(f'Noticia: {noticia_UOL.text}')
        web.lineEdit_6.setText(f'Noticia: {noticia_UOL2.text}')
        web.lineEdit_5.setText(f'Noticia: {noticiaTERRA.text}')
        x = 0


def cotação():
    newWindow.show()
    newWindow.setStyleSheet(open('style.css').read())
    newWindow.lineEdit.setText(f'{cotacao_dolar[0].text}')
    newWindow.lineEdit_2.setText(f'{cotacao_dolar[3].text}')
    newWindow.lineEdit_3.setText(f'{cotacao_libra.text}')



    


app = QtWidgets.QApplication([])
aplication = QApplication
mainwindow = QMainWindow
web = uic.loadUi("untitled.ui")
web.setStyleSheet(open('style.css').read())

newWindow = uic.loadUi("untitled2.ui")


web.pushButton.clicked.connect(uol_not)
web.pushButton_2.clicked.connect(trocar_cidade)
web.pushButton_6.clicked.connect(cotação)

web.show()
app.exec()