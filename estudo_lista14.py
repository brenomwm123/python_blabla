pega_nome = input('Informe os nomes separados por virgula: ')

lista_nome = pega_nome.split(',')
alfabetica = sorted(lista_nome)
contrario = sorted(lista_nome, reverse=True)

print(f'Lista com todos os nomes : {lista_nome}')
print(f'Lista com os nomes em ordem alfabetica: {alfabetica}')
print(f'Lista com os nomes em ordem alfabetica reversa: {contrario}')
print(f'Numero de nomes na lista: {len(lista_nome)}')