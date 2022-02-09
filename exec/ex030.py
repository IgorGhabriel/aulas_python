n0 = int(input('Digite um numero inteiro: '))
print(f'\nVocê digitou {n0}.\n')
r1 = n0 % 2
if r1 == 0:
    print(f'{n0} é um número par.\n')
else:
    print(f'{n0} é um número ímpar\n')