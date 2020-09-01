import time

def abririarquivo():
    try:
        arquivo = open('arquivodoido.txt')
        return True
    except Exception as err:

        print(f'Aconteu algum erro:{err}')
        return False

while not abririarquivo():
    print('Tentando abriri o arquivo ')
    time.sleep(5)

print('Consegui  abri o arquivo')

