nomes =['Joçao', 'Julia', 'Larissa', 'marcelo', 'Guilheme', 'Ramon']

lista_de_numeros = range(5, 10, 2)

for i in range(len(nomes)):
    print(nomes[i])
    nomes.append('Maria')

print(nomes, '\n')

i = 0

while i < 11:
    print('i ainda é menor do que 10:', i)
    i += 1

print('Agora i é meior do que 10\n')


lista_de_frutas = ['maçan', 'uva', 'pera', 'abacaxi', 'goiaba']

contador = 0

for fruta in lista_de_frutas:
    contador += 1

print('Vc tem ', contador, 'frutas\n')


numero = 0

'Verifica se a condição é verdadeira'
while True:

    'imprime o numero'
    print(numero)

    'verifica se o numer é igual a 20'
    if numero == 20:

        'caso número seja igua a 20 ela sai do loop, mesmo sendo ifinito'
        break

    'caso numero não seja igual 20 ele sai do for e adciona um valor a numero'
    numero += 1

'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas
que serão convidada para uma festa.
Ápos isso o programa irá pergunta o nome de todas as pessoas
e irá imprimi todos os nomes da lista 
'''








