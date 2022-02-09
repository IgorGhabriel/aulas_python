#Digitar varios numeros, guardar em uma lista
#se já tiver um numero igual, não adciona-lo a lista

valor = []

while True:
    v0 = int(input('Digite um valor: '))
    if v0 not in valor:
        valor.append(v0)
        print('Valor adicionado a lista.\n')
    else:
        print('Valor já existe na lista, então não foi adicionado.\n')
    again = input('Deseja continuar? [S/N] ').capitalize().strip()
    if 'S' in again:
        continue
    else:
        break
        

valor.sort()
print(f'\nOs valores adicionados na lista foram: {valor}')
