def mformat(p = 0, coin='R$'):
    return f'{coin}{p:>.2f}'.replace('.', ',')



def aumentar(p = 0, tsoma = 0, mformat = True):
    res = p + (p * tsoma / 100)
    if mformat in True:
        return mformat(res)
    else:
        return res


def diminuir(p = 0, tsub = 0, mformat = True):
    res = p - (p * tsub / 100)
    if mformat in True:
        return mformat(res)
    else:
        return res


def dobro(p = 0, mformat = True):
    res = p * 2
    if mformat in True:
        return mformat(res)
    else:
        return res


def metade(p = 0, mformat = True):
    res = p / 2
    if mformat in True:
        return mformat(res)
    else:
        return res


def resumo(p = 0, tsoma = 0, tsub = 0):
    print('')
    print('-' * 30)
    print(f'valor analisado: {mformat(p)}.')
    print('-' * 30)
    print(f'\nO dobro de {mformat(p)} é igual a: {dobro(p)}')
    print(f'A metade do valor {mformat(p)} é igual a: {metade(p)}')
    print(f'O valor {mformat(p)} com acréscimo de {mformat(tsoma)} é igual a: {aumentar(p, tsoma)}')