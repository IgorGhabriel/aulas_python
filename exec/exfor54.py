maior = 0
menor = 0

for i in range (1, 8):
    anonasc = int(input(f'\nDigite o ano de nascimento da {i}º pessoa: '))
    if anonasc <= 2003:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'\n{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.\n')

