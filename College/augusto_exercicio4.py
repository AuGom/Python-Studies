value = input('Digite a chave de entrada: ')
flag = 0
sample = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in value:
    if i in sample:
        flag += 1

if flag == 1:
    print("Chave correta.")
elif flag > 1:
    print("A chave possui mais de um interiro.")
else:
    print("A chave faltando o caracter numerico.")
