try:
    arquivo = "notas.txt"
    arq = open(arquivo, 'r')
    texto = arq.read()
except:
    print("Arquivo "+arquivo+" nao foi encontrado.")
