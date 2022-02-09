n = 0
multi = 1
rmulti = n * multi

while True:
    n = int(input('\nQuer ver a taboada de qual valor(Qualquer num negativo para parar): ' ))
    if n <= 0:
        break
    print('')
    for multi in range (1, 11):
        print(f'{n} x {multi} = {n * multi}')

print('\nENCERRADO\n')

