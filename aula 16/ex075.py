import random
numsort = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print('Numeros sorteados foram: ', end='')
for p in numsort:
    print(f'{p} ', end='')
print(f'\nO maior numero sorteado foi o {max(numsort)}')
print(f'O menor numero sorteado foi o {min(numsort)}\n')