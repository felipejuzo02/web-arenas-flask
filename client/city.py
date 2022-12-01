import requests
import json
from tabulate import tabulate
from termcolor import colored

headers = {"Content-Type": "application/json; charset=utf-8"}

def get_city():
    print('Consultando as cidades disponíveis...\n')
    request = requests.get('http://localhost:5000/city')
    arenas = json.loads(request.content)

    print(tabulate(arenas, headers={'id': 'Código', 'name': 'Nome', 'state': 'Estado'}))

def add_city():
    print('Para adicionar uma cidade, preencha as informações solicitadas.')
    name = input('Nome da cidade: ')
    state = input('Estado: ')

    try:
        data = {
            'name': name,
            'state': state
        }

        request = requests.post('http://localhost:5000/city', headers=headers, json=data)

        if request.json()["code"] == 200 or request.json()["code"] == 201:
            print(colored('\n ' + request.json()["message"], 'green'))
        else:
             print(colored('\n ' + request.json()["message"], 'red'))
    except Exception as error:
        print(colored('Erro ao adicionar cidade', 'red'))
        print(error)

def delete_city(id):
    try:
        request = requests.delete(f'http://localhost:5000/city/{id}')
    
        if request.status_code == 201:
            print(colored('Cidade excluida com sucesso!\n', 'green'))
        else:
            print(colored('Erro ao excluir', 'red'))

    except Exception:
        print(colored('Erro ao excluir', 'red'))
