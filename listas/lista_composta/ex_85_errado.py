##Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.


par = []
imp = []
#num = 0

for i in range (0,6):
    num = int(input(f'Informe o valor de numero {i+1}: '))
    if num % 2 == 0:
        if num not in par:
            par.append(num)
    else:
        if num not in imp:
            imp.append(num)

final_par = sorted(par)
final_imp = sorted(imp)
print(final_par)
print(final_imp)   