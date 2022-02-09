#ler nome e peso de varias pessoas, guardar tudo em UMA lista
#mostrar quantas pessoas foram cadastradas, lista de mais pesadas, lista de mais leves.

banco = []
dados = []

pesscad = 0

pmax = 0
pmin = 0

npmax = ''
npmin = ''

while True:
    dados.append(str(input('\nNome: ')))
    dados.append(float(input('Peso: ')))

    pesscad += 1

    if pmax == 0 and pmin == 0:
        pmax = dados[1]
        pmin = dados[1]
        npmax = dados[0]
        npmin = dados[0]

    if dados[1] > pmax:
        pmax = dados[1]
        npmax = dados[0]
    if dados[1] == pmax and dados[0] != npmax:
        npmax = npmax + ', ' + dados[0]
        
    if dados[1] < pmin:
        pmin = dados[1]
        npmin = dados[0]
    if dados[1] == pmin and dados[0] != npmin:
        npmin = npmin + ', ' + dados[0]

    banco.append(dados[:])
    dados.clear()

    seguir = str(input('\nDeseja continuar? [S/N] '))
    if seguir in 'Nn':
        break

print(f'\nEssas são as pessoas cadastradas: {banco}')
print(f'O número de pessoas cadastradas é igual a: {len(banco)}')
print(f'\nA ou as pessoas mais pesadas são: {npmax} pesando {pmax} KG.')
print(f'\nA ou as pessoas mais leves são: {npmin} pesando {pmin} KG.')
    







