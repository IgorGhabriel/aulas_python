
def mformat(p=0, coin='R$'):
    return f'{coin}{p:>.2f}'.replace('.', ',')


def aumentar(p=0, tsoma=0, formatar=True):
    res = p + (p * tsoma / 100)
    if formatar is True:
        return mformat(res)
    else:
        return res


def diminuir(p=0, tsub=0, formatar=True):
    res = p - (p * tsub / 100)
    if formatar is True:
        return mformat(res)
    else:
        return res


def dobro(p=0, formatar=True):
    res = p * 2
    if formatar is True:
        return mformat(res)
    else:
        return res


def metade(p=0, formatar=True):
    res = p / 2
    if formatar is True:
        return mformat(res)
    else:
        return res


def mresumo(p=0, tsoma=0, tsub=0):

    print(f'\nvalor analisado: {mformat(p)}.')

    print(f'\nO dobro de {mformat(p)} é igual a: {dobro(p)}')
    print(f'A metade do valor {mformat(p)} é igual a: {metade(p)}')
    print(f'O valor {mformat(p)} com acréscimo de {tsoma}% é igual a: {aumentar(p, tsoma)}')
    print(f'O valor {mformat(p)} tirando {tsub}% é igual a: {diminuir(p, tsub)}\n')
