##Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

##Funções
def sorteia():
    for i in range(5):
        num = randint(0, 10) 
        numeros.append(num)
    print(numeros)
def somaPar():
    s = 0
    for num in numeros:
        if num % 2 == 0:
            print(f'{num} é par.')
            s += num
            print(f'Soma atual: {s}')
    print(f'Soma final {s}')
        
    
#Codigo principal
from random import randint
numeros = []
sorteia()
somaPar()
