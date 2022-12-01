import requests
import json
from tabulate import tabulate
from termcolor import colored

headers = {"Content-Type": "application/json; charset=utf-8"}

def add_users():
    print('Para adicionar um usuário, preencha as informações solicitadas.')
    name = input('Nome: ')
    phone = input('Telefone: ')
    email = input('E-mail: ')
    document = input('CPF: ')
    city = input('Cidade: ')
    password = input('Senha: ')

    repeatPasswordBool = True
    while repeatPasswordBool:
        repeatPassword = input('Repita sua senha: ')

        if repeatPassword == password:
            repeatPasswordBool = False
        else:
            print(colored('\nSenhas não são iguais!! Digite novamente\n', 'red'))

    try:
        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'document': document,
            'city': city,
            'password': password
        }

        request = requests.post('http://localhost:5000/users', headers=headers, json=data)

        print(colored(request.json["message"], ('green' if request.status_code == 201 else 'red')))
    except Exception:
        print(colored('Erro ao adicionar', 'red'))

def get_users():
    try:
        print('Consultando os usuários cadastrados...\n')
        request = requests.get('http://localhost:5000/users')
        users = json.loads(request.content)

        if len(users):
            print(tabulate(users, headers={'id': 'Código', 'name': 'Nome', 'phone': 'Telefone', 'email': 'E-mail', 'document': 'CPF', 'city': 'Cidade'}))
        else:
            print('\nNenhum usuário encontrado!!\n')
    except Exception:
        print(colored('\nErro ao realizar a requisição\n', 'red'))

def get_user(id):
    try:
        request = requests.get(f'http://localhost:5000/user/{id}')
        user = request.json()

        return user
    except Exception:
        print(colored('\nErro ao realizar a requisição\n', 'red'))

def edit_information(value, user):
    try:
        data = {
            value: input('Digite o novo valor: ')
        }

        request = requests.put(f'http://localhost:5000/user/{user["id"]}', headers=headers, json=data)
        user = json.loads(request.content)

        if request.status_code == 201:
            print(user)
            print(colored('\nUsuário alterado com sucesso!', 'green'))
        else:
            print(colored('Erro ao excluir', 'red'))
    except Exception:
        print(colored('\nOcorreu um erro ao realizar a requisição: \n', 'red'))

def authenticate(user, password):
    params = {
        "username": user,
        "password": password
    }

    request = requests.get('http://localhost:5000/login', json=params)
    user = request.json()

    return user

def delete_user(id):
    try:
        request = requests.delete(f'http://localhost:5000/user/{id}')
    
        if request.status_code == 201:
            print(colored('Usuário excluido com sucesso!', 'green'))
        else:
            print(colored('Erro ao excluir', 'red'))

    except Exception:
        print(colored('Erro ao excluir', 'red'))
