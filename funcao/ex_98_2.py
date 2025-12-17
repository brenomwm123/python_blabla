from time import sleep

def linha():
    print('-='*15)
    
def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.1)
            c += passo
        print('   FIM')
        linha()
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.1)
            c -= passo
        print('   FIM')
        linha()
    
        
#Codigo principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Chegou sua vez.')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)