from PyQt5 import uic, QtWidgets #pip install PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
import time
from datetime import datetime

def receive_site_return_soup(site):
    searchings = requests.get(site)
    soup = BeautifulSoup(searchings.text,'html.parser')
    return soup 

###############-Temp. New Yor-k###############
soup = receive_site_return_soup('https://weather.com/weather/today/l/f892433d7660da170347398eb8e3d722d8d362fe7dd15af16ce88324e1b96e70')
cidade_NY = soup.find(class_='h4 today_nowcard-location')
temperatura_NYf = soup.find(class_='today_nowcard-temp') 
temperatura_NYf = temperatura_NYf.text.replace('°','')
temperatura_NYc = (((int(temperatura_NYf) - 32) * 5) / 9)
print('ok')
###############-Temp.London-###############
soup = receive_site_return_soup('https://weather.com/weather/today/l/UKXX0085:1:UK')
cidade_LO = soup.find(class_='h4 today_nowcard-location')
temperatura_LOf = soup.find(class_='today_nowcard-temp') 
temperatura_LOf = temperatura_LOf.text.replace('°','')
temperatura_LOc = (((int(temperatura_LOf) - 32) * 5) / 9)
print('ok')
###############-Temp. Juiz de Fora-###############
soup = receive_site_return_soup('https://weather.com/pt-BR/clima/hoje/l/BRXX0131:1:BR')
cidade_MG = soup.find(class_='h4 today_nowcard-location')
temperatura_MG = soup.find(class_='today_nowcard-temp')
print('ok')
###############-News Juiz de Fora-###############
soup = receive_site_return_soup('https://g1.globo.com/mg/zona-da-mata/cidade/juiz-de-fora/')
news_MG = soup.find('a',class_='feed-post-link gui-color-primary gui-color-hover')
news_MG_2 = soup.find_all('a',class_='feed-post-link gui-color-primary gui-color-hover')
print('ok')
###############-News New York-###############
soup = receive_site_return_soup('https://www.nytimes.com/')
NY_NEWS = soup.find_all('div',class_='css-1ez5fsm esl82me1')
print('ok')
###############-News London-###############
soup = receive_site_return_soup('https://www.bbc.com/news/england')
LONDON_NEWS = soup.find_all('a',class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')
print('ok')
###############-Temp.São Paulo-###############
now = datetime.now()
soup = receive_site_return_soup('https://weather.com/pt-BR/clima/hoje/l/S%C3%A3o+Paulo+S%C3%A3o+Paulo?canonicalCityId=d7593e91d7e1447404d3a75fc1f7e0513bfcc5bdd74b81f6b4299f68b5689392')
cidade = soup.find(class_='h4 today_nowcard-location')
temperatura = soup.find(class_='today_nowcard-temp')
print('ok')
###############-News UOL(Brasil)-###############
soup = receive_site_return_soup('https://www.uol.com.br/')
cabecalho_uol = soup.find(class_='chapeu color1')
noticia_UOL = soup.find('h1',class_='titulo color2')
noticia_UOL2 = soup.find('h2',class_='titulo color2')
print('ok')
###############-News Terra-###############
t = receive_site_return_soup('https://www.terra.com.br/')
noticiaTERRA = t.find('a',class_='main-url text')
print('ok')
###############-Cotação Dólar-###############
zzz = receive_site_return_soup('https://economia.uol.com.br/cotacoes/')
cotacao_dolar = zzz.find_all('a',class_='subtituloGrafico subtituloGraficoValor')
print('ok')
###############-Cotação Líbra-###############
soup = receive_site_return_soup('https://www.beecambio.com.br/cotacao/libra-esterlina')
cotacao_libra = soup.find('span',class_='currencyValue')
print('ok')
###################################################


###############-Edita a GUI com as noticias-###############
def uol_not():
    web.label.setText('Principais Noticias - UOL')
    web.lineEdit.setText(cidade.text)
    web.lineEdit_2.setText(f'Temperatura: {temperatura.text}')
    web.lineEdit_3.setText(f'{cabecalho_uol.text}')
    web.lineEdit_4.setText(f'Noticia: {noticia_UOL.text}')
    web.lineEdit_6.setText(f'Noticia: {noticia_UOL2.text}')
    web.lineEdit_5.setText(f'Noticia: {noticiaTERRA.text}')
    web.lineEdit_7.setText(f'{now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}:{now.second}')
###########################################################
    
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