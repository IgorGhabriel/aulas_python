num = int(input('\nDigite o numero que deseja fatorar: '))
c = num
f = 1
while c > 0:
    print(f'{c}')
    print(f' x ' if c > 1 else ' = ')

    f = f * c
    c = c - 1

print(f'{f}')

