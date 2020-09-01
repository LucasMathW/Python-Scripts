while True:
    c = 0
    nome = input('Quem é vc ?: ')
    if nome != 'Joe':
        continue

    print('Qual sua senha Joe (é um peixe): ')
    password = input()
    if password == 'peixespada':
        break
print('Acesso Garantido')
