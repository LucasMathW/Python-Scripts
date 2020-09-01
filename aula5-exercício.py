import sys
'''
EXERCICIO: Faça um programa que leia a quantidade de pessoas
que serão convidadas para uma festa.
Ápos isso o programa irá pergunta o nome de todas as pessoas
e irá imprimi todos os nomes da lista
'''

argumento = sys.argv


print('\n#######PROGRAMA DE GERÊNCIAMENTO DE CONVIDADOS DE FESTINHAS############')
print("#######################################################################\n")

#quantidade_de_convidados = int(argumento[1]) #input('Por Favor insira a quantidade de convidados: ')
lista_de_convidados = []

print('A FESTA TERÁ #', argumento[1], 'Convidados\n')

i = 1

while i <= int(argumento[1]):

    nome_do_convidado = input('Insira o nome do convidado #' + str(i) + ': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1


print('\nSEUS CONVIDADOS:')

contador = 1

for nome in lista_de_convidados:

    print('#' + str(contador) + '', nome)
    contador += 1



