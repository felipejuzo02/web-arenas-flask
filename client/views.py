from termcolor import colored

def login_menu():
    print('-----------------------------------------')
    print('------------ Seja Bem Vindo -------------')
    print('-----------------------------------------')

def admin_menu():
    print('\n-----------------------------------------')
    print('----------------- Menu ------------------')
    print('-----------------------------------------')
    print('[ 1 ] - Arenas Esportivas')
    print('[ 2 ] - Usuários')
    print('[ 3 ] - Cidades')
    print('[ 4 ] - Sobre')
    print('[ 5 ] - Exportar dados')
    print('[ 6 ] - Importar arenas de Ribeirão')
    print('[ 0 ] - Encerrar sistema')

def arenas_menu():
    print('-----------------------------------------')
    print('---------------- Arenas -----------------')
    print('-----------------------------------------')
    print('[ 0 ] - Voltar para menu anterior')
    print('[ 1 ] - Consultar arenas')
    print('[ 2 ] - Adicionar arena')
    print(colored('[ 3 ] - Excluir arena', 'red'))

def import_menu():
    print('-----------------------------------------')
    print('----------- Importar Arenas -------------')
    print('-----------------------------------------')
    print('[ 0 ] - Voltar para menu anterior')
    print('[ 1 ] - Importar arenas de Ribeirão Preto')
    print('[ 2 ] - Consultar arenas importadas')

def city_menu():
    print('-----------------------------------------')
    print('---------------- Cidades ----------------')
    print('-----------------------------------------')
    print('[ 0 ] - Voltar para menu anterior')
    print('[ 1 ] - Consultar cidades')
    print('[ 2 ] - Adicionar cidade')
    print(colored('[ 3 ] - Excluir cidade', 'red'))

def users_menu():
    print('-----------------------------------------')
    print('--------------- Usuários ----------------')
    print('-----------------------------------------')
    print('[ 0 ] - Voltar para menu anterior')
    print('[ 1 ] - Consultar usuários')
    print('[ 2 ] - Adicionar usuário')
    print('[ 3 ] - Editar usuário')
    print(colored('[ 4 ] - Excluir usuário', 'red'))

def about_text():
    print('-----------------------------------------')
    print('----------------- Sobre -----------------')
    print('-----------------------------------------')
    print('O Web Arenas é uma aplicação desenvolvida para facilitar a rotina dos atletas amadores e profissionais, através do rápido e fácil acesso a diversas Arenas e Quadras Esportivas, ajudando naquela partida entre os amigos.')
    print('Nosso objetivo é facilitar o aluguel de quadras, através do cadastro simples de Arenas, cadastro dos Jogadores, e acesso ao catálogo detalhado das Arenas disponíveis para locação.')
    print(colored('\nDesenvolvedores: \nBruno Populin - RA: 2840482013008\nLuis Felipe Juzo - RA: 2840482013015\n', 'yellow'))