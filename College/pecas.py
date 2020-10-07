pecas = {}
while True:
    cod = int(input('digite o codigo:'))
    if cod == 0:
        break
    elif cod in pecas:
        print('peca {} ja esta cadastrada'.format(cod))
        continue
    qtde = int(input('digite a quantidade:'))
    pecas[cod] = qtde
    print("estoque")
    for c in pecas:
        print("{1:4} unidades da peca {0}".format(c, pecas[c]))
