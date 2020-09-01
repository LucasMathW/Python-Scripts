minha_lista = ['luh', 'Julia']  # LISTA (list), tem índiçe
minha_tupla = ('luh', 'Julia')  # TUPLA (tuple), tem índiçe
meu_dicionario = {'nome': 'Lucas', 'idade': '27'}  #DICIONARIO (dict), não tem índiçe, sim chaves
meu_conjunto = {'Lucas', 'Ardaico'}  # CONJUTO (set), não tem índiçe AND não repete valores

########################## INICIANDO VAZIO ######################################

minha_lista = []
minha_tupla = ()
meu_dicionario = {}
meu_conjunto = set()

########################## ALINHANDO ESTRUTURAS DENTRO DE ESTRUTURAS##################

minha_lista = [(1, 2), (1, 3), {'nome': 'Jomara'}, {'Lucas'}]

print(minha_lista)


minha_tupla = ('João', 'Amarildo', 'Thiago')

if 'João' in minha_tupla:
    print('Está na Tupla')

else:

    print("Não está na coleção")

##################### DICIONÁRIO ########################

meu_dicionario['nome'] = 'Mario'  # MUDANDO VALOR DE CHAVE
meu_dicionario['endereço'] = 'Redenção'  # ADICIONANDO CHAVE COM VALOR

if 'Lucas' in meu_dicionario.values():
    print('Lucas está no dicionário\n')


if 'nome' in meu_dicionario.keys():
    print('esse valor exixte no dicionáio')

else:

    print('Valor não exixte')


for valor in meu_dicionario.values():
    print(valor)


#################### CONJUNTO ##################################

meu_conjunto.add('Maria')
meu_conjunto.add('Marcos')
meu_conjunto.add("Guilherme")

meu_conjunto.remove('Maria')

print(meu_conjunto)
