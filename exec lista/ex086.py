#fazer uma matriz 3x3;
#preencher com valores lidos pelo teclado;
#mostrar com a formatação correta a matriz preenchida;

matriz = [[], [], []]

set = -1
lin = 0
col = 0

for cont in range(0, 9):
    set = int(input(f'Digite o valor da posição {lin}x{cont-col}: '))
    matriz[lin].append(set)

    if cont == 2:
        lin += 1
        col += 3

    if cont == 5:
        lin += 1
        col += 3

print('')
print(matriz[0])
print(matriz[1])
print(matriz[2])
    
