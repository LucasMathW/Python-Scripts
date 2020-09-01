import requests
import json

def lista_filmes(nome):
    lista = []
    for i in range(1, 101):
        try:
            req = requests.get(f'http://www.omdbapi.com/?s={nome}&apikey=c009e037&type=movie&page={i}')
            resposta = json.loads(req.text)

            if resposta['Response'] == 'True':
              for filme in resposta['Search']:
                titulo = filme['Title']
                ano = filme['Year']
                string = titulo + '(' + ano + ')'
                lista.append(string)
              else:
                break
                print('Nenhum resultado encontrado')
        except:
            print('Falha na conexão')

    return lista

sair = False

while not sair:
    opc = input("Digite o nome do filme ou digite 'SAIR' para fechar o programa: ")
    if opc == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        lista_de_filmes = lista_filmes(opc)
        print('Resultados encontrados:', + len(lista_de_filmes))
        for filme in lista_de_filmes:
         print(filme)



'''
lista=[]

req = requests.get('http://www.omdbapi.com/?s=matrix&apikey=c009e037&type=movie&page=1')
resp = json.loads(req.text)
#print(resp)

if resp['Response'] == 'True':
    for i in resp['Search']:
         titulo = i['Title']
         ano  = i['Year']
         string = titulo + '(' + ano + ')'
         lista.append(string)

         for item in lista:
             print(item)
'''