import oauth2
import requests
import json
import urllib

class Twtter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.client = oauth2.Client(self.consumer, self.token)


    def serch(self, search, lang):
        search_codfcd = urllib.parse.quote(search, safe='')
        requisicao = self.client.request(f'https://api.twitter.com/1.1/search/tweets.json?q={search_codfcd}&lang={lang}')
        req_codificada = requisicao[1].decode()
        objeto = json.loads(req_codificada)
        twtters  = objeto['statuses']
        return twtters

    def post(self, new_post):
        new_postc = urllib.parse.quote(new_post, safe='')
        requisicao = self.client.request(f"https://api.twitter.com/1.1/search/tweets.json?q={new_postc}", method='POST')
        req_decoficada = requisicao[1].decode()
        objeto = json.loads(req_decoficada)
        return objeto





