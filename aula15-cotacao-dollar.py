import requests
import json
import time
import datetime

while True:
    resp = requests.get('https://api.hgbrasil.com/finance?format=json&key=48b098c0')
    resposta = json.loads(resp.text)
    tempo = datetime.datetime.now()

    print(f'########## VARIAÇÃO DO DOLLAR, BITCOIN E EURO ##############\n')
    print(f'DATA: {tempo}\n')

    print(f"Moeda: {resposta['results']['currencies']['USD']['name']}")
    print(f"Valor: {resposta['results']['currencies']['USD']['buy']}")
    print(f"Variação: {resposta['results']['currencies']['USD']['variation']}")

    print('+*'*30)

    print(f"Nome: {resposta['results']['currencies']['BTC']['name']}")
    print(f"Valor: {resposta['results']['currencies']['BTC']['buy']}")
    print(f"Variação: {resposta['results']['currencies']['BTC']['variation']}")

    print('+*' * 30)

    print(f"Nome: {resposta['results']['currencies']['EUR']['name']}")
    print(f"Valor: {resposta['results']['currencies']['EUR']['buy']}")
    print(f"Variação: {resposta['results']['currencies']['EUR']['variation']}")

    time.sleep(3)


