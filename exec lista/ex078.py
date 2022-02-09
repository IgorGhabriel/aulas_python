#ler 5 valores, guardar em UMA lista;
#mostrar o maior, menor, e suas respectivas posições na lista;

import numpy as np

valores = []


for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c+1}: ')))


valoresNP = np.array(valores)

maxv = max(valores)
minv = min(valores)
posmaxv = np.where(valoresNP == maxv)
posminv = np.where(valoresNP == minv) 


print(f'\nOs valores digitados foram: {valores}.')
print(f'\nO maior valor digitado foi o {maxv}, nas posições {posmaxv[0]} da lista.')
print(f'\nO menor valor digitado foi o {minv}, nas posições {posminv[0]} da lista.\n')
