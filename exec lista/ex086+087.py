#fazer uma matriz 3x3;
#preencher com valores lidos pelo teclado;
#mostrar com a formatação correta a matriz preenchida;

matriz = [[], [], []]

set = 0
pares = 0
soma3c = 0


for c in range(len(matriz)):

    for l in range(len(matriz)):
        set = int(input(f'L{l} x C{c}: '))
        matriz[c].append(set)
        if set % 2 == 0:
            pares += set
        if l == 2:
            soma3c += set
            print(soma3c)


for c in range(len(matriz)):
    
    for l in range(len(matriz)):
        print(f'[{(matriz[c] [l]):^5}]', end='')
    print('')

print(matriz[0])
print(matriz[1])
print(matriz[2])

print('')

print(f'A soma dos valores pares da matriz é igual a: {pares}.')
print(f'A soma dos valores da terceira coluna é: {soma3c}.')
print(f'O maior valor da segunda linha é: {max(matriz[1])}.\n')