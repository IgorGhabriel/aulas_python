#Ler vários numeros e guardar em UMA lista;
#criar uma lista para separar os valores impares e pares;
#mostrar as 3 listas;

lista = []
check = 0

par = []
impar = []

while True:
    check = int(input('\nDigite um número: '))
    lista.append(check)
    pos = 0
    while pos < len(lista):
        if check % 2 == 0:
            par.append(check)
            print(f'{check} foi adicionado à lista par.')
            pos += 1
        else:
            impar.append(check)
            print(f'{check} foi adicionado à lista ímpar.')
            pos += 1
        break
        
    seguir = str(input('Deseja continuar? [S/N] '))
    if seguir in 'Nn':
        break

print(f'\nOs números digitados foram: {lista}.')
print(f'\nOs números pares digitados foram: {par}.')
print(f'\nOs números ímpares digitados foram: {impar}.\n')