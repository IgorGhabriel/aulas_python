#ler nome e peso de varias pessoas, guardar tudo em UMA lista
#mostrar quantas pessoas foram cadastradas, lista de mais pesadas, lista de mais leves.

dado = []
banco = []

maxp = 0
minp = 0
nmaxp = ''
nminp = ''

while True:
    dado.append(str(input('\nNome: ')))
    dado.append(float(input('Peso: ')))

    # if maxp == 0 and minp == 0:
    #     nmaxp = dado[0]
    #     nminp = dado[0]
    #     maxp = dado[1]
    #     minp = dado[1]

    if dado[1] > maxp or maxp == 0:
        maxp = dado[1]
        nmaxp = dado[0]
    if dado[1] == maxp and dado[0] != nmaxp:
        nmaxp = dado[0] + ', ' + nmaxp

    if dado[1] < minp or minp == 0:
        minp = dado[1]
        nminp = dado[0]
    if dado[1] == minp and dado[0] != nminp:
        nminp = dado[0] + ', ' + nminp

    banco.append(dado[:])
    dado.clear()

    seguir = str(input('\nDeseja continuar? [S/N] '))
    if seguir in 'Nn':
        break

print(f'\nForam cadastradas {len(banco)} pessoas na lista.')
print(f'\nA ou as pessoas mais pesadas foram: {nmaxp} pesando {maxp} Kg.')
print(f'\nA ou as pessoas mais leves foram: {nminp} pesando {minp} Kg.\n')


    
