import oauth2
import requests
import json

consumer_key = 'WMMDkmklslssl!lmLKklmkm'
consumer_secret = "WALKSKLDKLhckeAJJLKJLKJLKJXJLKJZL"

token_key = 'QWERTYUISDFGHJKLXCVBNM'
token_secret = 'QWERTYUIOLKJHGFDSZXCVBhNM'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
clinte = oauth2.Client(consumer, token)


post = input('Digite seu Post')
reqisicao = clinte.request(f"https://api.twitter.com/1.1/statuses/update.json?status={post}", method='POST')
reqisicao_codificada = reqisicao[1].decode()

objeto = json.loads(reqisicao_codificada)
