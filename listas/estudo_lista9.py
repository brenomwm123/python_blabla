pegar_os_nome = input('Informe os nomes separados por virgula: ')

lista = pegar_os_nome.split(',')
nomes_com_a = []

for nome in lista:
    if nome.strip()[0] in 'Aa':
        nomes_com_a.append(nome)
        
print(f'Lista completa: {lista}')
print(f'Lista de pessoas com nomes que comecam com A: {nomes_com_a}')