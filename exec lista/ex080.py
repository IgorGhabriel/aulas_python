#ler 5 valores, guardar em UMA lista;
#Posicionar os valores na posição correta sem usar o sort();
#Mostrar os a lista ordernada;

valores = []

for c in range (0, 5):
    v0 = int(input('\nDigite um valor: '))
    if c == 0 or v0 > valores[-1]:
        valores.append(v0)
        print(f'{v0} foi adicionado na ultima posição da lista')
    else:
        pos = 0
        while pos < len(valores):
            if v0 <= valores[pos]:
                valores.insert(pos, v0)
                print(f'{v0} foi adicionado na posição {pos} da lista.')
                break
            pos += 1

print(f'\nOs valores digitados em ordem crescente ficam nessa ordem: {valores}.\n')

