lista = [] #listas são definidas por colchetes
            #listas são mutaveis, pode-se colocar mais itens e remover itens, até mesmo substituir itens;
lanche = ['pizza', 'suco', 'sorvete']

lanche.append('cookie') #pode-se adicionar itens em litas com o append
#append adiciona um elemento na ultima posição da lista

lanche.insert(0,'cahorro quente')
#com o comando insert adciona um elemento na posição declarada

del lanche[3] #deleta o elemento declarado da lista
lanche.pop(3) #deleta o ultimo elemento ou o elemento declarado
lanche.remove('pizza') #deleta o primeiro item com o nome declarado da lista, se tiver mais de um, só o primeiro será deletado, e reorganiza o índice;

if 'pizza' in lanche:
    lanche.remove('pizza')
#método para remover um item da lista caso ele exista;

valores = list(range(4,11)) #cria uma lista de forma crescente
#para criar uma lista desordenada, basta ir declarando itens de forma aleátoria

valoresRandom = [6, 3, 8, 9, 4, 2, 5, 11]
#para organizar a lista usa-se o comando sort
valoresRandom.sort()
#sort() vai deixar numeros em ordem crescente e strings em ordem alfabética

len(valores) #vai mostrar qnts itens tem na lista, do 0 ao ultimo item.
