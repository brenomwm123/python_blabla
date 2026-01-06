##Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#maior nota, menor nota, media da turma, situacao(opcional)

def notas(*n, sit=False):
    r = {}
    if len(n) == 0:
        return{}    
    
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = round(sum(n)/len(n), 2)
    
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOM'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'           
    return r
    
        
#Codigo principal
resposta = notas(5.5, 8.7, 9.0, 10.0, 1.5, 0.5, sit=True)
print(resposta)