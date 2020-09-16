import os
import pickle
os.chdir("C:\\Users\Augusto\Desktop\Python-Studies\College")

new_man = []

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('file error: ' + str(err))
except pickle.PickleErro as perr:
    print('pickling error: ' + str(perr))

print(new_man)
