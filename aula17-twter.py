import oauth2
import requests
import json
import urllib.parse

consumer_key = 'WMMDkmklslssl!lmLKklmkm'
consumer_secret = "WALKSKLDKLhckeAJJLKJLKJLKJXJLKJZL"

token_key = 'QWERTYUISDFGHJKLXCVBNM'
token_secret = 'QWERTYUIOLKJHGFDSZXCVBhNM'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

search = input('Pesquisa: ')
search_codfcd = urllib.parse.quote(search, safe='')
requisicao = client.request(f"https://api.twitter.com/1.1/search/tweets.json?q={search_codfcd}&lang=pt")

req_decodificada = requisicao[1].decode()

objeto = json.loads(req_decodificada)
twtters = objeto['statuses']

for tweeter in twtters:
    print (tweeter['user']['screen-name'])
    print (tweeter ['text'])
    print()