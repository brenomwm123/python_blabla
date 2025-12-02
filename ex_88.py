from random import randint

lista = list()
jogos = list()

print('=-' * 20)
print('CALCULANDO BI BU'.center(40))
print('=-' * 20)

quant = int(input('Informe quantos jogos voce quer: '))

tot = 1
while tot <= quant:
    c = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            c+=1
        if c == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print(f'SORTEANDO {quant} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
