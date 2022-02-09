#ler nome e peso de várias pessoas e guardar em UMA lista.
#Mostrar qnt pessoas cadastradas; os mais gordos; os mais leves

pessoas = []
dados = []

pesscad = 0

minp = -1
maxp = -1
nmaxp = ''
nminp = ''

while True:

    dados.append(str(input('\nNome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))

    pesscad += 1

    if dados[1] > maxp or maxp == -1:
        maxp = dados[1]
        nmaxp = dados[0]
    if dados[1] == maxp and dados[0] != nmaxp:
        nmaxp = nmaxp + ', ' + dados[0]

    if dados[1] < minp or minp == -1:
        minp = dados[1]
        nminp = dados[0] 
    if dados[1] == minp and dados[0] != nminp:
        nminp = nminp + ', ' + dados[0]

    pessoas.append(dados[:])
    dados.clear()

    again = str(input('\nContinuar? [S/N] ')).capitalize().strip()
    if 'S' in again or 'SIM' in again:
        continue
    else:
        break

print(pessoas)
print(f'\nNumero de pessoas cadastradas: {pesscad} pessoas.')
print(f'\nNome da(s) pessoa(s) mais pesada(s): {nmaxp} pesando {maxp} Kg.')
print(f'\nNome da(s) pessoa(s) mais leve(s): {nminp} pesando {minp} Kg.')



