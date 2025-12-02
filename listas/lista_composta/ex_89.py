#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Solução Alternativa para o Exercício Python 089

alunos = []

# Coleta de dados
while True:
    nome = str(input("Nome: ")).strip().capitalize()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    
    # Adiciona os dados na lista principal
    alunos.append([nome, n1, n2])
    
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == 'N':
        break

print("-=" * 25)

# 1. Exibição do Boletim
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>6}')
print("-" * 27)

for indice, aluno in enumerate(alunos):
    # A média é calculada aqui, na hora de exibir
    media = (aluno[1] + aluno[2]) / 2
    # aluno[0] é o nome
    print(f'{indice:<4}{aluno[0]:<15}{media:>6.1f}')

print("-" * 35)

# 2. Consulta de notas individuais
while True:
    num = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if num == 999:
        break
    
    if num >= 0 and num < len(alunos):
        # alunos[num][0] é o nome
        # alunos[num][1] é a nota 1
        # alunos[num][2] é a nota 2
        print(f"As notas de {alunos[num][0]} são: {alunos[num][1]} e {alunos[num][2]}")
        print("-" * 35)
    else:
        print("Aluno não encontrado. Tente um número válido da lista.")

print("Programa finalizado. Obrigado!")