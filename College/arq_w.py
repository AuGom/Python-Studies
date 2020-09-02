# arq = open("text.txt", 'w')
# for num in range(1, 10):
#     arq.write("*" * num + "\n")
# arq.close()

arq = open("text.txt", 'r')
linha = arq.readline()
while (linha != ""):
    print(linha)
    linha = arq.readline()

arq = open("text.txt", 'r')
linhas = arq.readlines()
cont = 0
while (cont < len(linhas)):
    print(linhas[cont])
    cont += 1
