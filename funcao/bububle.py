from uteis import numeros

#Codigo principal
print('-=' * 15)
num = int(input('Informe um valor: '))
fat=numeros.fatorial(num)
print('-=' * 15)
print(f'O fatorial de {num} é {fat}')
print('-=' * 15)
print(f'O dobro de {num} é {numeros.dobro(num)}')
print('-=' * 15)
print(f'O triplo de {num} é {numeros.triplo(num)}')
print('-=' * 15)