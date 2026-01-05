###Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')