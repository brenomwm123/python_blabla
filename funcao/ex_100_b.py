from random import randint

#Funções
def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 10))
    print(lista)
        
def somaPar(lista):
    s = 0
    for num in lista:
        if num % 2 == 0:
            print(f'{num} é par.')
            s += num
    print(f'A soma resultou em {s}')

#Codigo principal
numeros = []
sorteia(numeros)
somaPar(numeros)