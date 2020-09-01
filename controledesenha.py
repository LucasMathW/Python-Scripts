cont = 3

nome_int = input('Insira seu nome de usuário: ')

while nome_int != 'Lucas':

        nome_int = input(f'nome de usuário incorreto, tente mais: {cont}')

        cont = cont - 1

        if cont == 0:
            print('vc já tentou todas as auternativas, por favor tente mais tarde...')
            break

senha_int = input('Por favor insira sua senha: ')

if senha_int == 'senhateste':

    print('Acesso garantindo')

