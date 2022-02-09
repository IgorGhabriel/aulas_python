from tracemalloc import stop


num_extenso = 'zero', 'um', 'dois', 'trez', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'

while True:
    n0 = int(input('\nDigite um número entre 0 e 13: '))
    if n0 < 0 or n0 > 13:
        print('Tente novamente')
        continue
    
    print(f'Você digitou o número: {num_extenso[n0]}.\n')
    break