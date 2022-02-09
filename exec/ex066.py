cont = 0
n = 0
soma = 0
stop = 'break'

while True:
    n = int(input('Digite um número (Digite 999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
if cont >= 2:
    print(f'A soma doss {cont} números é igual a {soma}.')
else:
    print(f'Você só digitou 1 numero, que é {soma}.')

