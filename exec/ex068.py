import random
num = 0
res = ''
pcnum = 0
lado = ''

print('\nVAMOS JOGAR PAR OU ÍMPAR\n')

while True:
    pcnum = random.randint(0,9)
    num = int(input('\nEscolha um numero: '))
    lado = str(input('Par ou Ímpar? [P/I] ')).capitalize().strip()
    somanum = pcnum + num
    if somanum % 2 == 0:
        res = 'P'
        print(f'\nVocê jogou {num}, o pc jogou {pcnum}.\nO total é {somanum}, que é Par.')
    else:
        res = 'I'
        print(f'\nVocê jogou {num}, o pc jogou {pcnum}.\nO total é {somanum}, que é Impar.')
    if res == lado:
        print('\nVocê venceu, bora de novo...\n')
    else:
        print('\nperdeu, eu sou muito melhor que vc hahaha.')
        break

print('\nPrograma Encerrado\n')

