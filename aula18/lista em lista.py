galera = []
dado = []
for c in range (0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()