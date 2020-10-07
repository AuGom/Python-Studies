alunos = {}
while True:
    cod = int(input('digite a matricula:'))
    if cod == 0:
        break
    elif cod in alunos:
        print('aluno {} ja cadastrado'.format(cod))
        continue
    dictalu = {}
    dictalu['nome'] = input("digite o nome do aluno: ")
    dictalu['idade'] = int(input('digite a idade:'))
    dictalu['curso'] = input("digite o curso: ")
    alunos[cod] = dictalu
    print("alunos")
    for mat, data in alunos.items():
        print("Aluno: {}, mat:{}, idade:{}, curso:{}".format(
            data['nome'], mat, data['idade'], data['curso']))
