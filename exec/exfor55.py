maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}º pessoa, peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\nA pessoa com maior peso tem {maior}Kg.\nA pessoa com menor peso tem {menor}Kg.\n')