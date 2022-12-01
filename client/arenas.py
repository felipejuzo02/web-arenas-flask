import views as views
import requests
import json
from tabulate import tabulate
from termcolor import colored

headers = {"Content-Type": "application/json; charset=utf-8"}

def get_arenas():
    print('Consultando as arenas disponíveis...\n')
    request = requests.get('http://localhost:5000/arenas')
    arenas = json.loads(request.content)

    print(tabulate(arenas, headers={'id': 'Código', 'name': 'Nome', 'price': 'Preco', 'category': 'Categoria' ,'city': 'Cidade'}))

def add_arenas():
    print('Para adicionar arenas, preencha as informações solicitadas.')
    name = input('Nome da arena: ')
    category = input('Categoria: ')
    price = input('Preço: ')
    city = input('Cidade: ')
    
    try:
        data = {
            'name': name,
            'category': category,
            'price': price,
            'city': city
        }

        request = requests.post('http://localhost:5000/arenas', headers=headers, json=data)

        if request.json()["code"] == 200 or request.json()["code"] == 201:
            print(colored('\n ' + request.json()["message"], 'green'))
        else:
             print(colored('\n ' + request.json()["message"], 'red'))
    except Exception as error:
        print('Erro ao adicionar')
        print(error)


def delete_arena(id):
    try:
        request = requests.delete(f'http://localhost:5000/arena/{id}')

        if request.status_code == 201:
            print(colored('Arena excluida com sucesso!', 'green'))
        else:
            print(colored('Erro ao excluir', 'red'))

    except Exception:
        print(colored('Erro ao excluir', 'red'))
