from PyQt5 import uic, QtWidgets
import requests #pip install requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import random


weather_NY = 'https://weather.com/weather/today/l/f892433d7660da170347398eb8e3d722d8d362fe7dd15af16ce88324e1b96e70'
searching_6 = requests.get(weather_NY)
soup = BeautifulSoup(searching_6.text,'html.parser')
cidade_NY = soup.find(class_='h4 today_nowcard-location')
temperatura_NYf = soup.find(class_='today_nowcard-temp') 
temperatura_NYf = temperatura_NYf.text.replace('°','')
temperatura_NYc = (((int(temperatura_NYf) - 32) * 5) / 9)
#################################################################
weather_London = 'https://weather.com/weather/today/l/UKXX0085:1:UK'
searching_5 = requests.get(weather_London)
soup = BeautifulSoup(searching_5.text,'html.parser')
cidade_LO = soup.find(class_='h4 today_nowcard-location')
temperatura_LOf = soup.find(class_='today_nowcard-temp') 
temperatura_LOf = temperatura_LOf.text.replace('°','')
temperatura_LOc = (((int(temperatura_LOf) - 32) * 5) / 9)
#################################################################
weather_MG = 'https://weather.com/pt-BR/clima/hoje/l/BRXX0131:1:BR'
searching_4 = requests.get(weather_MG)
soup = BeautifulSoup(searching_4.text,'html.parser')
cidade_MG = soup.find(class_='h4 today_nowcard-location')
temperatura_MG = soup.find(class_='today_nowcard-temp')

def uol_not():
    now = datetime.now()
    weather = 'https://weather.com/pt-BR/clima/hoje/l/S%C3%A3o+Paulo+S%C3%A3o+Paulo?canonicalCityId=d7593e91d7e1447404d3a75fc1f7e0513bfcc5bdd74b81f6b4299f68b5689392'
    searching_2 = requests.get(weather)
    soup = BeautifulSoup(searching_2.text, 'html.parser')
    cidade = soup.find(class_='h4 today_nowcard-location')
    temperatura = soup.find(class_='today_nowcard-temp')
    ###################################################
    uol = 'https://www.uol.com.br/'
    searching = requests.get(uol)
    soup = BeautifulSoup(searching.text, 'html.parser')
    cabecalho_uol = soup.find(class_='chapeu color1')
    noticia_UOL = soup.find('h1',class_='titulo color2')
    noticia_UOL2 = soup.find('h2',class_='titulo color2')
    ####################################################
    terra = 'https://www.terra.com.br/'
    searching_3 = requests.get(terra)
    t = BeautifulSoup(searching_3.text, 'html.parser')
    noticiaTERRA = t.find('a',class_='main-url text')
    ###################################################
    web.lineEdit.setText(cidade.text)
    web.lineEdit_2.setText(f'Temperatura: {temperatura.text}')
    web.lineEdit_3.setText(f'{cabecalho_uol.text}')
    web.lineEdit_4.setText(f'Noticia: {noticia_UOL.text}')
    web.lineEdit_5.setText(f'Noticia: {noticiaTERRA.text}')
    web.lineEdit_6.setText(f'Noticia: {noticia_UOL2.text}')
    web.lineEdit_7.setText(f'{now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}:{now.second}')
    ###################################################
    

def trocar_cidade():
    sortear = [1,2,3]
    ra = random.choice(sortear)
    if ra == 1:
        web.lineEdit.setText(cidade_NY.text)
        web.lineEdit_2.setText(f'Temperatura: {int(temperatura_NYc)} ºC')
    if ra == 2:
        web.lineEdit.setText(cidade_LO.text)
        web.lineEdit_2.setText(f'Temperatura: {int(temperatura_LOc)} ºC')
    if ra == 3:
        web.lineEdit.setText(cidade_MG.text)
        web.lineEdit_2.setText(f'Temperatura: {temperatura_MG.text} ºC')





app = QtWidgets.QApplication([])
web = uic.loadUi("untitled.ui")
web.setStyleSheet(open('style.css').read())
web.pushButton.clicked.connect(uol_not)
web.pushButton_2.clicked.connect(trocar_cidade)


web.show()
app.exec()