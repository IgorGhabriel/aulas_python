#Ler 7 numeros, guardar em UMA lista, separando os ímpares e pares;
#mostrar em ordem crescente;

valores = []
par = []
impar = []
check = -1

for c in range (0, 7):
    check = int(input(f'\nDigite o {c+1}º número: '))
    valores.append(par)
    valores.append(impar)
    
    if check % 2 == 0:
        par.append(check)
    else:
        impar.append(check)

par.sort()
impar.sort()
print(f'{valores}')
print(f'\nOs valores pares digitados foram: {valores[0]}.')
print(f'\nOs valores ímpares digitados foram: {valores[1]}.\n')

