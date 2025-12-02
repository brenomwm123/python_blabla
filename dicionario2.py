estado = {}
brasil = []

for i in range(3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Informe a sigla do estado: '))
    brasil.append(estado.copy())
    
for e in brasil:
    for k, v in e.items():
        print(f'O estado {k} tem sigla {v}')