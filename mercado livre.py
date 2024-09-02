import requests
from bs4 import BeautifulSoup
import pandas as pd


url_base = 'https://lista.mercadolivre.com.br/'

produtonome = input('Qual produto você deseja? ')

response = requests.get(url_base + produtonome)

site = BeautifulSoup(response.text, 'html.parser')

#correcao 01: troca do "find" por "find_all" ja que sao diversos objetos(elementos html)
protutos = site.find_all('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in protutos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'}).text # adicionar o "".text" no final ja retorna o valor que eu quero sem precisar fazer tratamentos posteriores
    print(titulo)

    link = produto.find('a').get('href') # como so tem um unic0 link dentro do objeto produto eu vou direto no mesmo.
    print(link)

    preco = produto.find('span', class_='andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript').text # pego todo o texto dentro do span
    print(preco, '\n')