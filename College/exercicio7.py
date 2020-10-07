from os import truncate


arq = open("valores.txt", 'w')
while True:
    val = float(input('digite um valor:'))
    valf = round(val, 3)
    if valf == 0:
        break
    else:
        valstr = str(valf)
        arq.write(valstr+"\n")
arq.close()
