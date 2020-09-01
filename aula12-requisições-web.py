import requests #beateful Soup BS4: pip install bs4

cabecalho = { 'User-agent': 'Windows 12', 'Referer':'https://google.com', 'Cf_ipcountry':'US'}

meus_cooks = {'Ultima-visita':'10-10-2020'}

meus_dados = {'username': 'Lucas@baratheon', 'passworld':'092823842298'}

rqeuisicao = None

texto = None

try:

    requisicao = requests.post('https://putsreq.com/KKVPPFXv2lwuScR2L0gW', headers=cabecalho, cookies=meus_cooks, data=meus_dados)
    texto = requisicao.text

except Exception as erro:

    print(f" Ocorreu um erro: {erro} ")

print(texto)