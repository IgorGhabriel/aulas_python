# #Ler 7 numeros, guardar em UMA lista, separando os ímpares e pares;
# #mostrar em ordem crescente;

# lista = []

# check = 0

# pares = 0
# impares = 0

# for c in range(0, 7):
#     check = int(input(f'Digite o {c+1}º número: '))

#     if check % 2 == 0:
#         lista.insert(0, check)
#         pares += 1

#     else:
#         lista.insert(-1, check)
#         impares += 1

# print(lista)
# print(pares)
# print(impares)
# print(f'\nOs números pares são: {sorted(lista[0:pares])}')
# print(f'\nOs números ìmpares são: {sorted(lista[impares -1:len(lista)])}')

lista = []

for i in range(0, 7):
    num = int(input('Digite: '))

    lista.append(num)

lista.sort()
for i in range(0,7):
    if lista[i] % 2 == 0:
        print(lista[i], end=', ')
print('')
for i in range(0,7):
    if lista[i] % 2 != 0:
        print(lista[i], end='')
