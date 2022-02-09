# pessoas = {'nome': 'Igor', 'sexo': 'M', 'idade': 18}

# #print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')

# #print(pessoas.keys()) #mostra os índices

# #print(pessoas.values()) #mostra o valor que está nos índices do dict

# #print(pessoas.items() )#mostra tudo 

# for k, v in pessoas.items():
#     print(f'\n{k} = {v}')


# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# for i in range (0, len(brasil)):
#     print('')
#     print(f'Estado: {brasil[i]["uf"]}', end=', ')
#     print(f'Sigla: {brasil[i]["sigla"]};')
#     print('')


estado = dict()
bra = list()

for i in range(0, 3):
     estado['uf'] = str(input('\nUnidade Federativa: '))
     estado['sigla'] = str(input('Sigla do Estado: '))
     bra.append(estado.copy())
     estado.clear()

for j in bra:
    for v in j.values():
        print(v, end=' - ')
    print('')