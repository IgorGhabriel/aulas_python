def area(l, c):
    final = l * c
    print(f'\nA área do terreno de {l}m de largura x {c}m de comprimento é igual a: {final}m².\n')


l = float(input('\nQual a largura do terreno? '))
c = float(input('\nQual é o comprimento do terreno? '))
area(l, c)
