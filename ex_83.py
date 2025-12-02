##Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha = []

exp = str(input('Informe uma expresssao matematica: '))

for caractere in exp:
    
    if caractere == '(':
        pilha.append(caractere)
        
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
        
if len(pilha) == 0:
    print('Deu certo')
else:
    print('Deu errado')