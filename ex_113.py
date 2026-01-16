
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
            n = float(input('Informe um numero inteiro: '))
        except(ValueError, TypeError):
            print('ERRO, não foi digitado um numero inteiro')
            continue
        else:
            return n


# Programa principal
leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')