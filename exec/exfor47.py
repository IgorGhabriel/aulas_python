import time
n0 = int(input('\nDigite o número que vai começar a contagem: '))
n1 = int(input('Digite o número em que a contagem vai parar: '))
print('')
for teta in range(n0, n1+1):
    if teta % 2 == 0:
        print (teta)
    time.sleep(0.2)
print('\nacabou\n')