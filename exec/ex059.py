import time
n1 = 0
n2 = 0

rr = 0
cc = 0
pp = ''

while pp != 'S':
    if n1 == 0 and n2 == 0:
        n1 = int(input('\nDigite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    print('\nPressione [1] para somar os valores;')
    print('Pressione [2] para multiplicar os valores;')
    print('Pressione [3] para mostrar qual dos valores é maior;')
    print('Pressione [4] para colocar novos numeros;')
    print('Pressione [5] para sair do programa;')
    cc = int(input('\nQual opção deseja escolher: '))
    
    if cc == 1:
        rr = n1 + n2
        print(f'\n{n1} + {n2} = {rr}')
        time.sleep(1)
        print('\nPressione [1] para somar os valores;')
        print('Pressione [2] para multiplicar os valores;')
        print('Pressione [3] para mostrar qual dos valores é maior;')
        print('Pressione [4] para colocar novos numeros;')
        print('Pressione [5] para sair do programa;')
        cc = int(input('\nQual opção deseja escolher: '))

    elif cc == 2:
        rr = n1 * n2
        print(f'\n{n1} x {n2} = {rr}')
        time.sleep(1)
        print('\nPressione [1] para somar os valores;')
        print('Pressione [2] para multiplicar os valores;')
        print('Pressione [3] para mostrar qual dos valores é maior;')
        print('Pressione [4] para colocar novos numeros;')
        print('Pressione [5] para sair do programa;')
        cc = int(input('\nQual opção deseja escolher: '))

    elif cc == 3:
        if n1 > n2:
            rr = print(f'\n{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'\n{n2} é maior que {n1}')
        elif n1 == n2:
            print(f'\nOs valores são iguais.')
        time.sleep(1)
        print('\nPressione [1] para somar os valores;')
        print('Pressione [2] para multiplicar os valores;')
        print('Pressione [3] para mostrar qual dos valores é maior;')
        print('Pressione [4] para colocar novos numeros;')
        print('Pressione [5] para sair do programa;')
        cc = int(input('\nQual opção deseja escolher: '))

    elif cc == 4:
        n1 = int(input('\nDigite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        time.sleep(1)
        print('\nPressione [1] para somar os valores;')
        print('Pressione [2] para multiplicar os valores;')
        print('Pressione [3] para mostrar qual dos valores é maior;')
        print('Pressione [4] para colocar novos numeros;')
        print('Pressione [5] para sair do programa;')
        cc = int(input('\nQual opção deseja escolher: '))
 
    elif cc == 5:
        pp = 'S' 



print('\nfim')