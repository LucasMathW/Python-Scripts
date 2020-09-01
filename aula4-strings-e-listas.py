
'AULA 4 - LISTAS E STRINGS'

frase =  "Ola, tudo bem?"
lista_nomes = ['lucas', 'Matheus', 'Ardaico', 'Ramon', 'Ramirez']

'imprimindo valores indicando o valor inicial(0) e final(15) do índice, e o passo(2)'
print (frase[0:15:2], '\n')

'imprimindo valores de trás para a frente'
print (lista_nomes[-1: -6: -1], '\n')

'invertendo a lista '
print(frase[::-1], '\n')

'adiçionando e removendo um item na lista'
lista_nomes.append("Jomara")
lista_nomes.append("Lorena")
lista_nomes.append('Lorena')
lista_nomes.remove('Jomara')

'inserindo um item na lista especificando a posição'
lista_nomes.insert(1, 'Creosvaldo')

'inserindo um item na lista sobrepondo um valor '
lista_nomes[0] = 'Penisvaldo'

'conta quantos valores repetidos exixtem na listas'
contador_Lorena = lista_nomes.count('Lorena')


'remove o ultimo iítem da lista e imprime ele sózinho, e sim por diante em forma de pilha '
print(lista_nomes.pop())
print(lista_nomes.pop())
print(lista_nomes.pop())
print(lista_nomes.pop(), '\n')

'imprimindo toda a frase em minusculo'
print(frase.lower())

frase_separada = frase.split(',')
print(frase_separada)



