pessoa = 1
idade = 0   
sexo = '' 

pessoas_mais18 = 0

num_Homens = 0

num_MulheresMenos20 = 0

cont = ''

while True:
    idade = int(input(f'\nIdade da {pessoa}º pessoa: '))
    sexo =  str(input(f'Sexo da {pessoa}º pessoa: [M/F] ')).capitalize().strip()
    pessoa += 1

    if idade > 18:
        pessoas_mais18 += 1

    if sexo in 'FFeminino' and idade < 20:
        num_MulheresMenos20 += 1

    if sexo in 'MMasculino':
        num_Homens = num_Homens + 1

    cont = str(input('\nDeseja continuar? [S/N] ')).capitalize().strip()
    if cont in 'NNão':
        break

print(f'\nVc digitou os dados de {pessoa-1} pessoas para analize.\n')
print(f'Das {pessoa-1} pessoas, {pessoas_mais18} tem mais de 18 anos.')
print(f'Das {pessoa-1} pessoas, {num_Homens} são homens.')
print(f'Das {pessoa-1} pessoas, {num_MulheresMenos20} são mulheres e tem menos de 20 anos.\n')


    




