import random as rdm
n0 = rdm.randint(0, 5)
r1 = int(input('\nPensei em um número entre 0 e 5, advinhe qual: '))
if r1 == n0:
    print('\nAcertou!\n')
    exit()
else:
    r2 = int(input('\nErrou... tenta de novo, tem mais 2 chances: '))
if r2 == n0:
    print('\nAcertou!\n')
    exit()
else:
    r3 = int(input('\nErrou... Última chance: '))
if r3 == n0:
    print('\nNa ultima conseguiu... Parabéns\n')
    exit()
else:
    print(f'\nA resposta certa é {n0}.\n')