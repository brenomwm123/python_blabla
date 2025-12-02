produtos = {}
media_preco = 0
maior = 0
menor = 9999999999999999999999999999999999
nome_maior = nome_menor = 0

while True:
    nome_produto = input('Informe o nome do produto: ')
    produtos[nome_produto] = int(input(f'Informe o preço do {nome_produto}: '))
    resp = input('Deseja adicionar outro produto ? [s/n]: ')
    if resp in 'Nn':
        break

print(produtos)

for k, v in produtos.items():
    media_preco = sum(produtos.values())/len(produtos)

for nome, preco in produtos.items():
    if preco > maior:
        maior = preco
        nome_maior = nome
    
    if preco < preco_menor:
        preco_menor = preco
        nome_menor = nome
        
print(f'O produto mais caro foi {nome_maior} custando {maior}')
print(f'O produto mais barato foi {nome_menor} custando {menor}')       
    
        
print(f'A media de preço dos produtos foi {media_preco}.')

