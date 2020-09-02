import os
os.getcwd()
os.chdir("C:\\Users\Augusto\Desktop")
os.getcwd()

# if os.path.exists('sketch.txt'):
try:
    data = open('sketch.txt')
# print(data.readline(), end='')
# data.seek(0)
# for i in data:
#     print(i, end='')
# data.close()

# for i in data:
#     if not i.find(':') == -1:
#         (role, line) = i.split(':', 1)
#         print(role, end='')
#         print(" disse: ", end='')
#         print(line, end='')
# data.close()

    for i in data:
        try:
            (role, line) = i.split(':', 1)
            print(role, end='')
            print(" disse: ", end='')
            print(line, end='')
        except:
            pass
    data.close()
except:
    print("caminho nao existe")
