import random

def pegueNumero(answerNumber):
    if answerNumber == 1:
        return 'Erro tente novamente'
    if answerNumber == 2:
        return 'tente mais uma vez  '
    if answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(0,9)
print(pegueNumero(r))