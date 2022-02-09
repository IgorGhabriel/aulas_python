v = int(input('Qual é a velocidade do carro no momento? '))
v_limite = int(input('Qual é o limite de velocidade nesta via? '))
print(f'\nVocê está andando a {v}Km/H, o limite de velocidade nesta via é de {v_limite}Km/H.\n')
if v <= v_limite:
    print(f'Ok, vc não vai ser multado se continuar nesta velocidade.\n')
else:
    print(f"""Caso vc passe por um radar uma multa no valor de R${((v - v_limite) * 6.99) + 195.00:.2f} vai chegar pra tu.
Diminua a velocidade em no mínimo {v - v_limite}Km/H para não ser multado.\n""")