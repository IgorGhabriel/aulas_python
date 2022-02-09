vcasa = float(input('\nQual é o valor da casa?R$ '))
vsalario = float(input('\nQual é o valor do seu salário? '))
tpagamento = int(input('\nEm quantos anos é planejado pagar o empréstimo? '))
vprestacao = vcasa / (tpagamento*12)
vprestacaomax = vsalario * 0.3

print(f'\nOlá, com um salário no valor de R${vsalario:.2f} o valor das prestações não pode ultrapassar {vprestacaomax:.2f}/Mês.')
if vprestacao <= vprestacaomax:
    print(f'O empréstimo com valor mensal de {vprestacao:.2f} pode ser aceito.\n')
else:
    print(f'\nO empréstimo não pode ser feito pois a prestação no valor de {vprestacao:.2f} excede o valor máximo de 30% em relação ao seu salário.\n')