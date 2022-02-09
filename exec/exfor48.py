n0 = int(input('Numero que começa: '))
n1 = int(input('\nNumero que termina: '))
resultado = 0
print('')
for conta in range (n0, n1+1):
    if conta % 2 != 0 and conta % 3 == 0:
        resultado = resultado + conta
print(resultado)
print('\nCabou\n')