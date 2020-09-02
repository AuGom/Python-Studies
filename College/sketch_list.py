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
