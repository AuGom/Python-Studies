entrada = input("Digite um valor entre 0 e 100: ")
num = int(entrada)
if not 0 < num < 100:
    print("invalido")
if num % 2 == 0:
    print("par")
if num % 2 != 0:
    print("par")
