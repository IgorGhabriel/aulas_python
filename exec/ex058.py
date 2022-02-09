import random
n0 = random.randint(1, 10)
print('\nUm número aleátorio entre 1 e 10 foi sorteado\n')
res = 0
qres = 1
while res != n0:
    res = int(input('Advinhe o número sorteado: '))
    if res != n0:
        print('\ntente novamnente.')
        qres = qres + 1
if qres == 1:
    tqres = 'primeira'
else:
    tqres =(f'{qres}º') 
print('Acertou.')
print(f'\nVc acertou na {tqres} alternativa.\n')