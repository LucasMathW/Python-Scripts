import twtter_lib

consumer_key = 'WMMDkmklslssl!lmLKklmkm'
consumer_secret = "WALKSKLDKLhckeAJJLKJLKJLKJXJLKJZL"

token_key = 'QWERTYUISDFGHJKLXCVBNM'
token_secret = 'QWERTYUIOLKJHGFDSZXCVBhNM'

twtter = twtter_lib.Twtter
twtter_pesquisa = twtter(consumer_key, consumer_secret, token_key, token_secret)

pesquisa = input('INSIRA O QUE VC QUER ENCONTRAR')

twtter_pesquisa.serch(pesquisa, 'pt')

for twtter in twtter_pesquisa:
    print(twtter['user']['screen'])
    print(twtter['text'])
    print()


twtter_post = twtter(consumer_key, consumer_secret, token_key, token_secret)
post = input('Escreva seu post aqui')

print(twtter_pesquisa.post(post))

