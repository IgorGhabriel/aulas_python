#ler VARIOS = nome, nota 1, nota 2, guardar em UMA lista composta;
#mostrar numero do aluno, NOME, MÈDIA das 2 notas;
#permitir mostrar as notas individuais de cada aluno;

banco = []
nome = []
notas = []
aluno = []

space = ''
while True:
    nome.append(str(input('\nNome: ')).capitalize().strip()) # - banco[al][0] *numero da pessoa
    notas.append(float(input('Nota 1: '))) # - banco[al][1][0]
    notas.append(float(input('Nota 2: '))) # - banco[al][1][1]
    notas.append((notas[0] + notas[1]) / 2.) #média - banco[al][1][2]

    aluno.append(nome[:])
    nome.clear()
    aluno.append(notas[:])
    notas.clear()
    banco.append(aluno[:])
    aluno.clear()

    seguir = str(input('\nDeseja continuar? [S/N] '))
    if seguir in 'Nn':
        break

print('-'*50)

for al in range(0, len(banco)):
    for name in range(al, len(banco)):
        name = ''.join(banco[al][0])
    print(f'{al} - nome: {name:^10}|{space:^3}média: {banco[al][1][2]:^4}')

print('-'*50)

while True:
    alu = int(input('\nDeseja mostrar a nota de qual aluno [-1 para parar]: '))

    if alu == -1:
        print('\nPrograma encerrado.')
        break

    name = ''.join(banco[alu][0])
    print(f'As notas de {name}: {banco[alu][1][0]}, {banco[alu][1][1]}')
    

print('-'*50)

