import math
num = int(input('\nvalor: '))
res = '\nÉ primo'
final = round((num/2)+1)
if num == 0 or num == 1:
    print('\nNão é primo')
else:
    for i in range(2, final):
        if num % i == 0:
            res = '\nNão é primo'
            break
print(res)