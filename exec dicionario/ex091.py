import random
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': random.randint(1, 6),
        'jogador 2': random.randint(1, 6),
        'jogador 3': random.randint(1, 6),
        'jogador 4': random.randint(1, 6)}

ranking = list()



print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\nRANKING FINAL!\n')

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

print('')