# Exemplo de uma função que soma dois número
def soma(numer1, numero2):
    resp = numer1 + numero2
    return resp

retorno = soma(1289, 75)

print(retorno)

# EXEMPLO E FUNÇÃO QUE IMPRIME UMA FRASE "OI'
def imprime_oi():
    print("OI")


print(imprime_oi())

#EXEMPLO DE FUNÇÃO QUE VERIFICA SE UM ITEM TEM SETE LETRAS
def tem_sete_item(item):

    if len(item) == 7:

        return True

    else:

        return False

if tem_sete_item([1,2,3,4,5,6,7]):
    print("Tem sete item")

'''
EXERCICIO: Escreva uma função que recebe um objeto de coleção e 
retorn o valor do maior numero dentro dessa coleção
faça outra função que retorne o menor numero dessa coleção 
'''