data = open('augusto.txt')

for i in data:
    if not i.find(',') == -1:
        (role, line) = i.split(',', 1)
        print(role + line)
    else:
        print(i)
data.close()
