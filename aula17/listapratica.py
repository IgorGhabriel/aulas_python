
num = [2, 5, 9, 1]

#num.append(7) #add o 7 na lista, automaticamente no ultimo lugar;

#print(f'\nA lista1: {num}')

#num.sort(reverse=True)

#print(f'\nA lista2: {num}')
#print(f'\nA lista em ordem crescente: {sorted(num)}')
#print(f'\nA liste em ordem decrescente: {numdescrescente}')
#num.sort()
#print(num)
                                                
#print(f'\nMostrar a quantidade de elementos da lista: {len(num)}')

valores = []
valores.append(1)
valores.append(9)
valores.append(5)

print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} da lista, tem o valor: {v}.')

print('\nFim da lista')

valorescop = valores[:]

valorescop.sort()
print(f'lista valores: {valores} ')
print(f'lista valorescopia: {valorescop} ')