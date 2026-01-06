##Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#maior nota, menor nota, media da turma, situacao(opcional)

def notas(*n, sit=False):
    print(n)
    
    
    
    
#Codigo principal
notas(5.5, 8.7, 9.0, 10.0, 1.5, 0.5, sit=True)