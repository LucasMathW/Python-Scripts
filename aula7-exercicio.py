
import sys
'''
EXERCICIO: Escreva uma função que recebe um objeto de coleção e
retorn o valor do maior numero dentro dessa coleção
faça outra função que retorne o menor numero dessa coleção

argumento = sys.argv

lista_num = []

mai = 0
men = 0

for c in range(0, int(argumento[1])):

    lista_num.append(int(input(f' Digite um valor para a posição {c}: ')))

    if c == 0:

        mai = men = lista_num[c]

    else:
        if lista_num[c] > mai:
            mai = lista_num[c]
        if lista_num[c] < men:
            men = lista_num[c]

print('=-' * 30)
print(f'vc digitou os valores  {lista_num}')
print('=-' * 30)
print(f'O maior valor nessa lista é {mai} ná posição', end='')
for i, v in enumerate(lista_num):
    if v == mai:
        print(f'...{i}', end='')

print(f'\nO maior valor nessa lista é {men} ná posição', end='')
for i, v in enumerate(lista_num):
    if v == men:
        print(f'...{i}', end='')
'''

#Função para ver a maior itemm dentro de uma lista

def maiori(lista):
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item

    return maior


#Função para ver o menor itemm dentro de uma lista

def menori(lista):
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item

    return menor

colecao = [21,2,3,4,5,6,7,8,9,10]

resp = menori(colecao)

print(resp)

