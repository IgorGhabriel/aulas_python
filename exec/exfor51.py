a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for pa in range (1, 11):
    x = a1 + ((pa - 1) * r)
    print(f'termo {pa} = {x}')