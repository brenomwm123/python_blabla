##Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
     nome = input('Informe seu nomeeee:  ')
     nota1 = float(input('Informe a primeira nota:  '))
     nota2 = float(input('Informe a segunda nota:  '))
     media = (nota1 + nota2)/2
     alunos.append([nome, [nota1, nota2], media])
     
     resp = input('Deseja adicionar outro aluno ?? \n[S/N]: ')
     if resp in 'Nn':
         break


print('-=' * 25)

print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>8}')

for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8}')

while True:
    resp = (input('Deseja consultar a nota de um dos alunos ? [S/N]: '))
    if resp in 'Nn':
        break
    else:
        cod = int(input('Informe o codigo do aluno:  '))
        if cod < len(alunos):
            print(f'Notas do(a) aluno {alunos[cod][0]}: {alunos[cod][1]}')   
        else:
            print('Codigo INVALIDO')     
        
    
        