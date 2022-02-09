n = int(input('\nDigite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

pa = 0
tt = 0
padrãopedido = 10
novopedido = 0
while tt < padrãopedido:
    pa = n + ((tt + 1)* r)
    print(f'termo {tt + 1} = {pa - r}')
    tt = tt + 1
    if tt >= tpedido:
        npedido = int(input('\nGostaria de ver mais quantos termos: '))

        tpedido = novopedido + padrãopedido
   
print('\nFIM\n')