nome = str(input('\nDigite o seu nome: '))
tudomaiusc = nome.upper()
tudominusc = nome.lower()
firstnomelista = nome.split()
firstnome = firstnomelista[0]
contarfirstnome = len(firstnome)

nomesemespaço =  nome.replace(' ', '')
contarallnome = len(nomesemespaço)


print(f'\nOlá, {nome}, o seu nome com todas as letras maiúsculas é {nome.upper()}.\nO seu nome com todas as letras minúsculas é {nome.lower()}')
print(f"""\nO seu primeiro nome é {firstnome}.\nO seu primeiro nome tem {contarfirstnome} caracteres.\nO seu nome completo tem {contarallnome} caracteres, sem contar os espaços.
Contando os espaços o seu nome tem {len(nome.strip())} caracteres.\n""")
