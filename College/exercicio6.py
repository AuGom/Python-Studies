frase = input("Digite uma frase: ")
arq = open("arquivo.txt", 'w')
arq.write(frase)
arq.close()
