pessoas = {'nome': 'Breno','sexo': 'masculino','idade': 22}
print('-='*15) 
 
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print('-='*15) 
 
print(pessoas.keys())
print('-='*15) 
 
print(pessoas.items())
print('-='*15) 
 
print(pessoas.values()) 
print('-='*15) 
 
for k in pessoas.keys():
    print(k)
print('-='*15)
  
for k in pessoas.values():
    print(k)
print('-='*15) 

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-='*15)
 
     
