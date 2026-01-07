import uteis

#Codigo principal
print('-=' * 15)
num = int(input('Informe um valor: '))
fat=uteis.fatorial(num)
print('-=' * 15)
print(f'O fatorial de {num} é {fat}')
print('-=' * 15)
print(f'O dobro de {num} é {uteis.dobro(num)}')
print('-=' * 15)
print(f'O triplo de {num} é {uteis.triplo(num)}')
print('-=' * 15)