def gugumilo(txt):
    tamanho = len(txt)
    linha = tamanho + 4
    print('~'*linha)
    print(f'{txt:^{linha}}')
    print('~'*linha)


#Começo do codigo    
gugumilo('jamelao peidao')
gugumilo('breno')
gugumilo('esquibidi dob')