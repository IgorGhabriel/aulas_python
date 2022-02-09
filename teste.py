def aumentar(p=0, psoma=0, formatar=True):
    res = p + (p * psoma/100)
    return res if formatar is False else coinformat(res)


def diminuir(p=0, psub=0, formatar=True):
    res = p - (p * psub/100)
    return res if formatar is False else coinformat(res)


def dobro(p=0, formatar=True):
    res = p * 2
    return res if formatar is False else coinformat(res)


def metade(p=0, formatar=True):
    res = p / 2
    return res if formatar is False else coinformat(res)


def coinformat(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def mresumo(p=0, psoma=0, psub=0):
    print('-'*30)
    print(f'O valor a ser analisado é o {coinformat(p)}.')
    print('-'*30)
    print(f'\nO dobro de {coinformat(p)} é igual a {dobro(p)}')
    print(f'A metade de {coinformat(p)} é igual a {metade(p)}')
    print(f'Com um acréscimo de {psoma}% ao valor de {coinformat(p)} fica igual a {aumentar(p, psoma)}')
    print(f'Com um desconto de {psub}% ao valor de {coinformat(p)} fica igual a {diminuir(p, psub)}\n')
    print('-'*30)


print(mresumo(1000, 50, 20))