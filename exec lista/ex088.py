#ler quantos jogos serão gerados;
#cada jogo sorteando 6 numeros de 1 a 60 sem repetição;
#mostrar e guardar em apenas uma lista composta;

import random as rdm
import time as time


jogo = []
banco = []

numjogos = int(input('\nQuantos jogos deseja fazer? '))

for i in range(0, numjogos):
    while True:
        check = rdm.randint(1, 60)
        if check not in jogo:
            jogo.append(check)

        if len(jogo) == 6:
            break


    
    jogo.sort()
    #print(f'O resultado do {i+1}º jogo: {jogo}.\n') #para não precisar criar uma outra lista, dar print antes de dar clear na lista;
    banco.append(jogo[:])
    jogo.clear()


print(f'\nForam feitos {numjogos} jogos, como pedido.')
for nj in range(0, numjogos):
    print(f'O resultado do {nj+1}º jogo: {banco[nj]}.\n')
    time.sleep(1)
