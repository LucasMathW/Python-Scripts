import re
import requests

string_de_teste = 'O gata é Bonito'
string_de_teste2 =  'O gato, a gata, os gatinhos, os gatoes, o gat'

requisicao = requests.get('https://www.lacoxinha.com.br/')


padrao = re.search(r'\w\w\w\w', string_de_teste)
padrao2 = re.findall(r'\w{4,6}', string_de_teste2)

padrao_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

if padrao:
    #print(padrao.group())
    print(padrao_email)
else:
    print('Padrão não encontrado ')

