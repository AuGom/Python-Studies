estacao = ["primavera", "verao", "outono", "inverno"]
for i in estacao:
    print(i)
print(len(estacao))
estacao.append("oi")
print(estacao)
estacao.pop()
print(estacao)
estacao.extend(["olha eu", "denovo"])
print(estacao)
estacao.remove("verao")
print(estacao)
estacao.insert(0, "roi")
print(estacao)
