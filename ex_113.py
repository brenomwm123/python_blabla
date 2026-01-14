
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')

def leiaFloat(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')