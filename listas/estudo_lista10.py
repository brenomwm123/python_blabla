from time import sleep

lista1 = []
lista2 = []

for num in range(5):
    valor = int(input('Informe um valor: '))
    lista1.append(valor)
    
print('\nPRIMEIRA LISTA PREENCHIDA.\nSOLICITANDO VALORES PARA SEGUNDA LISTA')

for num in range(5):
    valor = int(input('Informe um valor: '))
    lista2.append(valor)

print(f'PRIMEIRA LISTA {lista1}')
print(f'SEGUNDA LISTA {lista2}')

print('\nCONCATENANDO LISTAS...')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')

print(f'LISTAS CONCATENADAS: {lista1+lista2}')
print('CALCULANDO TAMANHO DA LISTA FINAL...')
sleep(1)
print('.')
sleep(1)
print('.')
print(f'a lista contem {len(lista1+lista2)} items.')
