import os
import pickle
os.chdir("C:\\Users\Augusto\Desktop\Python-Studies\College")

os.getcwd()

man = []
other = []

try:
    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_man_data.txt', 'wb') as other_file:
        pickle.dump(other, other_file)
except IOError as err:
    print('file error: ' + str(err))
except pickle.PickleErro as perr:
    print('pickling error: '+str(perr))
