# Comprações:  ==, !=, >, <, >=, <=
# Logicos: and, or

''' OPERADORES ĹÓGICOS

var_verdaede = True
var_false = False

a = 30
b = 20

if ((a>b) and ('Jão' == 'Jão')) or (3 == 2):

    print(a, 'é maior do que', b)

else:

    print('não deu certo o if')
'''



'''
print('OPÇÕES:\n\n 1 = Matheus\n 2 = Marcelo\n 3 = Josana')

opcao = input("\nEscolha uma opção:")

if opcao == '1':
    print('vc escolheu o Matheus')
elif opcao == '2':
    print('vc escolheu o Marcelo')
elif opcao == '3':
    print('vc escolheu a Josana')
else:
    print('Opcão Invalida')



    EXERCICIO-3
    
    Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
    e decida se ela esta apta a entrar no Exército. Para entrar no Exército
    é preciso tem mais de 18 anos, pesar mais ou igual a 60 kg e medir 1.70
    de altura     
    '''

print('ALISTAMENTO MILITAR 2018')

opcao_sexo = input('\n1-MASCULUINO \n2-FEMENINO\n')

if opcao_sexo == '1':

    print('\nvocê escolheu a opção número 1 que equivale á sexo masculino\n')

    opcao_idade = input('Digite sua idade:')
    opcao_peso = input('Digite seu peso:')
    opcao_altura = input('Digite sua altura:')

    if opcao_idade >= '18' and opcao_peso >= '60' and opcao_altura >= '1.70':

        print('\nvocê está apto a servi as forças armadas')

    else:

        print('\nVocẽ não está apto a servi')

elif opcao_sexo == '2':

    print('\nvocê escolheu a opção número 1 que equivale á sexo femenino\n')

    opcao_idade = input('Digite sua idade:')
    opcao_peso = input('Digite seu peso:')
    opcao_altura = input('Digite sua altura:')

    if opcao_idade >= '18' and opcao_peso >= '50' and opcao_altura >= '1.60':

        print("\nvocê está apta a servi as forças armadas")

    else:

        print('\nVocẽ não está apta a servi')
