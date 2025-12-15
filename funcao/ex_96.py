
def bloco(texto):
    print('-='*20)
    print(f'{texto:^40}')
    print('-='*20)
    
    
def área(l, c):
    area = l * c
    print(f'A area de um terreno de {l} por {c} é de {area:.2f}m2.')


#Codigo principal

bloco('Programa medidor de terreno')

l = float(input('Informe a largura do terreno: '))
c = float(input('Informe o comprimento do terreno: '))

área(l, c)


    
