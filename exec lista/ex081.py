#ler varios numeros e guardar em UMA lista;
#mostrar quantos numeros foram digitados; lista em ordem descrescente; se o valor 5 foi digitado;

valores = []

numsdig = 0

num5 = 'Não, não foi digitado'


while True:
    valores.append(int(input('\nDigite um número: ')))

    if 5 in valores:
        num5 = 'Sim, foi digitado'

    numsdig += 1

    seguir = str(input('Deseja continuar? [S/N] ').strip())
    if seguir in 'Nn':
        break

valoresDec = valores[:]
valoresDec.sort(reverse= True)

print(f'\nOs números digitados foram: {valores}.')
print(f'\nForam digitados {numsdig} números ao total.')
print(f'\nOs números digitados em ordem decressente é: {valoresDec}.')
print(f'\nO número 5 foi digitado? {num5}.\n')


