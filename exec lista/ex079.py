#Ler vários numeros e guardar em uma lista;
#não incluir numeros repetidos;
#mostrar os numeros adicionados, em ordem crescente;

nums = []
num0 = -1

while True:
    num0 = int(input('\nDigite um numero: '))

    if num0 in nums:
       print('Esse número ja existe na lista, então não será adcionado.')
    else:
        nums.append(num0)
        print('O número foi adicionado com sucesso!')
    
    seguir = str(input('\nDeseja continuar? [S/N] ').strip().capitalize())
    if 'S' in seguir or 'SIM' in seguir:
        continue
    else:
        break

print(f'\nOs valores selecionados foram: {nums}.')
print(f'\nOs valores selecionados em ordem crescente são {sorted(nums)}\n')

