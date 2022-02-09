#ler 5 valores, guardar em UMA lista;
#no FINAL mostrar o maior, menor e a posição de cada valor respectivamente;

valor = []

for v in range(0, 5):
    valor.append(int(input('Digite um valor: ')))

vmax = max(valor)
vmin = min(valor)
print(f'você digitou os valores: {valor}.')
print(f'\nO maior valor é: {vmax}, e está na posição {valor.index(vmax)+1}')
print(f'\nO menor valor é: {vmin}, e está na posição {valor.index(vmin)+1}')


