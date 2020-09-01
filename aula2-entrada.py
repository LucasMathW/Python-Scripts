'''ENTRADA DE DADOS:

#nome = input(' Por favor digite seu nome: ')
#idade = input(' agora digite sua idade: ')
#altura = input(' e por ultimo, a  autura: ')

tipo = type(nome)
tipoIdade = type(idade)
tipo_autura = type(altura)

##FORMA_1 DE CONCATENAR VARIAVEIS
#print(nome, 'tem', idade, 'de idade e', altura, 'de autura')

##FORMA_2 DE CONCATENAR VARIAVEIS
frase = (nome + ' tem ' + str(idade) + ' de idade e ' + str(altura) + ' de autura')

print(frase)

'''

'''CALCULADORA

numero1 = 50
numero2 = 16
numero3 = 25
numero34 = 1

resp = numero2 ** (1/2)

print('resposta', resp)

'''

''' EXERCICIO - 1: Faça um formulário que pergunta
o nome, cpf, endereço, idade, altura e telefone
e imprima isso de forma organizada '''


print('Por favor, preencha o formulário de inscrição abaixo')

nome = input('nome:')
idade = input('idade:')
altura = input('altura:')
cpf = input('cpf:')
telefone = input('telefone:')
endereco = input('endereço:')

print('\n Verifique se todos os Seus dados estão corretos, antes de enviar o formulário!\n')

print('## DADOS PESSOAIS ##'
      '\n NOME:', nome,
      '\n IDADE:', idade,
      '\n ALTURA:', altura,
      '\n CPF:', cpf,
      '\n TELEFONE:', telefone,
      '\n ENDEREÇO:', endereco)