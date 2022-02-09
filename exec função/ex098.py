def contador(i=0, f=0, p=0):
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1

    if i < f:
        res = i
        while res <= f:
            print(f'{res}', end=', ')
            res += p
            if res >= f + 1:
                print(' FIM! ')
                print('')

    else:
        res = i
        while res >= f:
            print(f'{res}', end=', ')
            res -= p
            if res <= f - 1:
                print(' FIM! ')
                print('')


contador(1, 10, 1)
print('')
contador(10, 0, 2)
print('')
i = int(input('Numero inicial da contagem: '))
f = int(input('Numero final da contagem: '))
p = int(input('Fazer a contagem de quanto em quanto? '))
contador(i, f, p)