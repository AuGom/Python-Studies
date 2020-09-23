n = int(input('Digite quantos valores voce deseja na sequencia: '))
n1 = int(0)
n2 = int(1)

if n < 0:
    print('Valor invalido.')
elif n < 2:
    print('Necessario no minimo dois valores.')
else:
    for i in range(n):
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
