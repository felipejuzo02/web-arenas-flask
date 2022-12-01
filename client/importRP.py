from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate
from termcolor import colored
import requests
import json

URL = 'https://www.encontraribeiraopreto.com.br/l/locacao-de-quadra-em-ribeirao-preto.shtml'
HEADERS = {"Content-Type": "application/json; charset=utf-8"}

def import_arenas():
    print('\nImportando dados...\n')

    arenas = []
    response = urlopen(URL)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    all_spans = soup.find_all('span')

    for value in all_spans:
        word = str(value)
        word = word.replace('<span class="style4">', "" )
        word = word.replace('</span>', "" )

        if len(word):
            if '<span' not in word:
                arenas.append(word)

    save_data(arenas)

def save_data(data):
    request = requests.post('http://localhost:5000/arenas-rp', headers=HEADERS, json=data)
    print(request.content)

def get_arenas_rp():
    try:
        print('\nBuscando dados importados...\n')
        request = requests.get('http://localhost:5000/arenas-rp')
        arenas_rp = json.loads(request.content)

        if request.status_code == 200:
            print(tabulate(arenas_rp, headers={'id': 'Código', 'name': 'Nome'}))
        else:
            print(colored('\nErro ao buscar arena\n', 'red'))
    except Exception:
        print(colored('\nErro ao buscar arena\n', 'red'))