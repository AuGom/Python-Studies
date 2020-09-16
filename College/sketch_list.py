man = []
other = []
try:
    data = open('sketch.txt')
    for i in data:
        try:
            (role, line) = i.split(':', 1)
            line = line.strip()
            if role == "Man":
                man.append(line)
            elif role == "Other Man":
                other.append(line)
        except ValueError:
            pass
    data.close()
except IOError:
    print("Arquivo nao existe")
print(man)
print(other)

with open('man_data.txt', 'w') as man_file:
    print(man, file=man_file)
with open('other_man_data.txt', 'w') as other_man_file:
    print(other, file=other_man_file)
