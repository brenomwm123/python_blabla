num = [[],[]]

for c in range(0,7):
    val = int(input('Informe um valor: '))
    if val % 2 == 0:
        if val not in num[0]:
            num[0].append(val)
    else:
        if val not in num[1]:
            num[1].append(val)

final_par = sorted(num[0], reverse=True)
final_imp = sorted(num[1], reverse=True)
print(f'Lista decrescente dos valores pares: {final_par}')
print(f'Lista decrescente dos valores impares: {final_imp}')   