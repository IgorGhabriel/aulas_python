sex = 'sex'
while sex != 'M' and sex !='F':
    sex = str(input('\nQual é o seu sexo? [M/F] ')).strip().capitalize()
    if sex != 'M' and sex !='F':
        print('Digite M ou F (M para masculino e F para feminino) corretamente.')
print(f'\nVocê é do sexo {sex}.')

