nome = str(input('Qual é o seu nome? ')).strip
print(f'Bom dia {nome}')
if nome == 'Igor':
    print('ok.')
elif nome == 'igor':
    print('ok.')
else:
    print('não ok.')