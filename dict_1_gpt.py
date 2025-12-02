alunos = {
    'joao': [9.4, 2.3, 10 ],
    'pablo': [1.0, 1.0, 10.0],
    'breno': [1.0, 5.0, 9.8]
    }

maior_media = 0
aluno_maior_media = 0
soma = 0

print('-='*20)

for k, v in alunos.items():
    media = sum(v)/len(v)
    if media > maior_media:
        maior_media = media
        aluno_maior_media = k
        
    print(f'A media do {k} foi {media:.2f}')

print('-='*20)

print(f'A maior media foi do {aluno_maior_media}, com uma media de {maior_media:.2f}')