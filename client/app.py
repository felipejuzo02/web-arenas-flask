import views as views
import arenas as arenas
import export as export
import importRP as importRP
import city as city
import users as users
from termcolor import colored
import os

CURRENT_USER = {}

def show_current_user():
    print('\nInformações do usuário')
    print(f'[ 1 ] Nome: {CURRENT_USER["name"]}')
    print(f'[ 2 ] Telefone: {CURRENT_USER["phone"]}')
    print(f'[ 3 ] E-mail: {CURRENT_USER["email"]}')
    print(f'[ 4 ] CPF: {CURRENT_USER["document"]}')
    print(f'[ 5 ] Senha: {CURRENT_USER["password"]}')
    print(f'[ 6 ] Cidade: {CURRENT_USER["city"]}')

run_system = False
while run_system == False:
    views.login_menu()
    username = input('Usuário: ')
    password = input('Senha: ')

    user = users.authenticate(username, password)
    if len(user):
        welcome = '\nSeja bem vindo, ' + user[0]["name"]
        CURRENT_USER = user[0]

        print(colored(welcome, 'green'))
        run_system = True

    else:
        print(colored('\nUsuário ou senha inválido!!\n', 'red'))

while run_system:
    try:
        views.admin_menu()
        opcao = int(input('Escolha uma opcao: '))
        os.system('cls')

        if opcao == 1:
            try:
                views.arenas_menu()
                answer = int(input('Escolha uma opcao: '))

                if answer == 1:
                    arenas.get_arenas()
                elif answer == 2:
                    arenas.add_arenas()
                elif answer == 3:
                    arenas.get_arenas()
                    try:
                        arena_to_delete = int(input('\nPara excluir uma arena, informe seu CÓDIGO: '))

                        arenas.delete_arena(arena_to_delete)
                    except ValueError:
                        print(colored('\nValor digitado não é um número!!', 'red'))

                elif answer == 0:
                    continue
                else:
                    print(colored('\nDigite uma opcao válida!!\n', 'red'))
            except ValueError:
                print(colored('\nValor digitado precisa ser um número!!\n', 'red'))

        elif opcao == 2:
            try:
                views.users_menu()
                answer = int(input('Escolha uma opcao: '))

                if answer == 1:
                    users.get_users()
                elif answer == 2:
                    users.add_users()
                elif answer == 3:
                    show_current_user()
                    try:
                        information_to_edit = int(input('Qual informação deseja editar: '))

                        dictionary = { 1: 'name', 2: 'phone', 3: 'email', 4: 'document', 5: 'password', 6: 'city' }

                        if 1 <= information_to_edit <= 6:
                            users.edit_information(dictionary[information_to_edit], CURRENT_USER)
                            CURRENT_USER = users.get_user(CURRENT_USER["id"])
                        else:
                            print(colored('\nFavor digitar uma valor válido\n'))
                    except ValueError:
                        print(colored('\nValor digitado não é um número!!', 'red'))
                elif answer == 4:
                    users.get_users()
                    try:
                        user_to_delete = int(input('\nPara excluir um usuário, informe seu CÓDIGO: '))

                        users.delete_user(user_to_delete)
                    except ValueError:
                        print(colored('\nValor digitado não é um número!!', 'red'))
                elif answer == 0:
                    continue
                else:
                    print(colored('\nDigite uma opcao válida!!\n', 'red'))
            except ValueError:
                print(colored('\nValor digitado precisa ser um número!!\n', 'red'))

        elif opcao == 3:
            try:
                views.city_menu()
                answer = int(input('Escolha uma opcao: '))

                if answer == 1:
                    city.get_city()
                elif answer == 2:
                    city.add_city()
                elif answer == 3:
                    city.get_city()
                    city_to_delete = input('\nPara excluir uma cidade, informe seu CÓDIGO: ')
                    city.delete_city(city_to_delete)
                    
                elif answer == 0:
                    continue
                else:
                    print(colored('\nDigite uma opcao válida!!\n', 'red'))
            except ValueError:
                print(colored('\nValor digitado precisa ser um número!!\n', 'red'))

        elif opcao == 4:
            views.about_text()
            os.system('pause')

        elif opcao == 5:
            export.export_files()
            os.system('pause')

        elif opcao == 6:
            try:
                views.import_menu()
                answer = int(input('Escolha uma opcao: '))

                if answer == 1:
                    importRP.import_arenas()

                elif answer == 2:
                    importRP.get_arenas_rp()

                elif answer == 0:
                    continue
                else:
                    print(colored('\nDigite uma opcao válida!!\n', 'red'))
                os.system('pause')
            except ValueError:
                print(colored('\nValor digitado precisa ser um número\n'))

        elif opcao == 0:
            invalid_anwser = True
            while invalid_anwser:
                response = input('\nDeseja realmente sair?? [s/n]: ')
                if response in ('s', 'S'):
                    run_system = False
                    invalid_anwser = False
                elif response in ('n', 'N'):
                    invalid_anwser = False
                    os.system('cls')
                else:
                    print(colored('\nDigite apenas [s] ou [n]\n', 'red'))
    except ValueError:
        print(colored('\nValor deve ser um número\n', 'red'))