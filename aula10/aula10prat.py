
nota1 = float(input('Nota de mat na primeira unidade: '))
nota2 = float(input('Nota de mat na segunda unidade: '))
nota3 = float(input('Nota de mat da terceira unidade: '))
media = ((nota1 + nota2 + nota3) / 3)
print(f'sua média foi de {media:.1f};')
if media == 6.0:
    print(f'passou no limite.')
elif media > 6.0 and media < 8.0:
    print(f'passou ok.')
elif media > 8.1 and media <= 9.9:
    print(f'passou bem.')
elif media == 10.0:
    print(f'parabéns, {media:.1f}, estudou oq sabe.')
else:
    print('estuda mais que ta triste.')


