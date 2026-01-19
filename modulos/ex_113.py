
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
numreal = leiaFloat('Digite um número: ')

print('-='*15)
print(f'{"OS NUMEROS DIGITADOS FORAM:":^30}')
print('-='*15)

print(f'NUMERO REAL: {numreal}')
print(f'NUMERO INTEIRO: {numint}')