import json
import requests
from termcolor import colored
import zipfile as zip

def export_files():
    try:
        datas = ['users', 'arenas', 'city']
        print('\nExportando arquivos...\n')

        for entity in datas:
            endpoint = f'http://localhost:5000/{entity}'

            request = requests.get(endpoint)
            data = json.loads(request.content)

            file_way = f'exported-files/{entity}.json'
            f = open(file_way, "w")
            json.dump(data, f, sort_keys=True, indent=4)
            f.close()

        zip_files()
        print(colored('Arquivos exportados com sucesso!!\n', 'green'))
    except Exception:
        print(colored('\nErro ao exportar arquivos\n', 'red'))

def zip_files():
    f = zip.ZipFile('exported-files/zipped-files.zip', 'w', zip.ZIP_DEFLATED)
    f.write('exported-files/users.json')
    f.write('exported-files/city.json')
    f.write('exported-files/arenas.json')
    f.close()
