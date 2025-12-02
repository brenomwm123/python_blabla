##Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


alunos = {}
alunos['nome'] = input('Informe o nome do individuo: ')
alunos['media'] = float(input('Informe a media do individuo: '))

if alunos['media'] < 5.0:
    alunos['situação'] = 'reprovado'
elif 5.0 <= alunos['media'] < 7.0:
    alunos['situação'] = 'recuperação'
elif alunos['media'] >= 7.0:
    alunos['situação'] = 'aprovado'
    
print('-='*15)
print(f'O {alunos["nome"]} ficou com media {alunos["media"]}, portanto está {alunos["situação"]}')
