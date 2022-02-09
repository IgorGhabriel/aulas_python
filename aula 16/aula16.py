#TUPLE
#Manipula a tuple como manipula uma string normal.
#Tuples são imutáveis.

#lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#print(lanche[1])
#print('\nfim\n')

#for cont in range(0, len(lanche)):
    #print(lanche[cont])
#print('\nfim2\n')

#for comida in lanche:
    #print(comida)
#print('\nfim3\n')

#for pos, comida in enumerate(lanche):
    #print(f'{comida}, posição:{pos}')
#Faça assim para numerar os itens da tuple;

#print(sorted(lanche)) #Usar o sorted faz a tuple virar uma list;
#print('')
#print(lanche)

a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b #isso coloca o resultado da tuple B junto do resultado da A.

print(c.count(5)) #Isso conta a quantidade do item pedido dentro da tuple.

print(c.index(8)) #Isso mostra em que posição o item pedido está dentro da tuple.

print(c)
del c
print(c)

