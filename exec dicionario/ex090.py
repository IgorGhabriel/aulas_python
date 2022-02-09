#ler nome e a média de um aluno; 7> aprovado;
#guardar situação(aprovação/reprovação) em dicionário;

aluno = {}

aluno['nome'] = str(input('\nNome do aluno: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}? '))

if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'

print(f'\nO aluno {aluno["nome"]}, com sua média de {aluno["média"]} foi {aluno["situação"]}.\n')
 