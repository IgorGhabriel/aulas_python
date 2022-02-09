

pessoa = {}
banco = []

while True:
    pessoa['nome'] = str(input('\nNome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))

    banco.append(pessoa.copy())
    pessoa.clear()

    seguir = str(input('\nDeseja continuar? [S/N] ')).strip()
    if seguir in 'Nn':
        break

cIdade = 0
for ci in range(0, len(banco)):
    cIdade = cIdade + banco[ci]['idade'] 
mIdade = cIdade / len(banco)

amIdade = []
for ami in range(0, len(banco)):
    if banco[ami]['idade'] > mIdade:
        amIdade.append(banco[ami]['nome'])

fem = []
for mu in range(0, len(banco)):
    if banco[mu]['sexo'] in 'Ff':
        fem.append(banco[mu]['nome'])



print(f'\nNo total, foram cadastrados {len(banco)} pessoa(s).')
print(f'\nA média de idade do grupo é de {mIdade} anos de idade.')
print(f'\nDas pessoas cadastradas, as mulheres são: {fem} ')
print(f'\nAs pessoas que tem idade acima da média de idade do grupo são: {amIdade}.\n')

