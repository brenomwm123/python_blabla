
def leiaInt(msg):
    while True:
        try:
            n = int(input('Informe um numero inteiro: '))
        except(ValueError, TypeError):
            print('ERRO, não foi digitado um numero inteiro')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input('Informe um numero real: '))
        except(ValueError, TypeError):
            print('ERRO, não foi digitado um numero real')
            continue
        else:
            return n


# Programa principal
numint = leiaInt('Digite um número: ')
print(f'Você digitou o número {numint}')
numreal = leiaFloat('Digite um número: ')
print(f'Você digitou o número {numreal}')