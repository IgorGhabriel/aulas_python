midade = 0
idademvelho = 0
nmvelho = ('|Não tem homens no grupo|')
qidadef = 0

for c in range (1, 5):
    print(f'\nPessoa n.{c}:')
    nome = str(input(f'\nNome: ')).strip().capitalize()
    idade = int(input(f'idade: '))
    sex = str(input(f'Sexo [M/F]: '))
    midade = midade + idade
    if c == 1 and sex == 'M':
       idademvelho = idade
       nmvelho = nome
    elif sex == 'M' and idade > idademvelho:
        idademvelho = idade
        nmvelho = nome    
    else:
        if sex == 'F' and idade < 20:
            qidadef = qidadef + 1

midadeg = midade / 4
print(f'\nMedia de idade do grupo: {midadeg:.1f} anos.')
print(f'Nome do homem mais velho: {nmvelho}.')
if qidadef > 1:
    mm = 'mulheres'
else:
    mm = 'mulher'
print(f'Quantidade de mulheres com menos de 20 anos: {qidadef} {mm}.\n')