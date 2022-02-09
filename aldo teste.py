r = 1
n_t = 0

while n_t != -1:
    res_aldo = 0
    res_beto = 0
    soma_beto = 0
    soma_aldo = 0

    res_r =''

    r = int(input(''))
    if r == 0:
        break
    elif r != 0:
        n_t = n_t + 1
    for r in range (0, r):
        res_aldo = int(input(''))
        res_beto = int(input(''))
        soma_aldo = soma_aldo + res_aldo
        soma_beto = soma_beto + res_beto


    print(f'\nTeste: {n_t}')
    if soma_aldo > soma_beto:
        res_r = 'Aldo'
    else:
        res_r = 'Beto'
    
    print(res_r)
    
    


