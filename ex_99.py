##Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    if len(num) == 0:
        print('Nenhum valor informado.')
    else:
        print(f'Os valores informados foram: {num}')
        print(f'O maior foi {max(num)}')
        print()
    
    
    
#Programa principal
maior(4, 6, 2, 4, 6, 6 ,8)
maior(1, 7, 2, 9)
maior(1, 5, 3)
maior(4)
maior()

    