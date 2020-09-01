import requests
import json

def requisicao(titulo):

    try:

        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=c009e037&type=movie')
        dicionario = json.loads(req.text)
        return dicionario

    except:

        print("Erro de requisição")
        return False

def printar_detalhes(filme):

    print(f" Título: {filme['Title']}")
    print(f" Atores: {filme['Actors']}")
    print(f" Ano: {filme['Year']}")
    print(f" Diretot: {filme['Director']}")
    print(f" Premios:{filme['Awards']}")
    print(f" Poster:{filme['Poster']}")


sair = False

while not sair:

    opc = input("Digite o nome de um filme ou SAIR para encerrar: ")

    if opc == 'SAIR':
        sair = True
        print('Saindo...')

    else:
        filme = requisicao(opc)
        if filme['Response'] == 'False' and filme['Error'] == 'No API key provided.':

            print("Filme Não encontrado")
            print('Ou o limite de solicitações diarias foi atingido')
        else:
            printar_detalhes(filme)

