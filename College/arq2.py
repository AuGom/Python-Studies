def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return (None)


def into_dict(data):
    d_data = {}

    d_data['nome'] = data.pop(0)
    d_data['nasc'] = data.pop(0)
    d_data['tempo'] = data

    return d_data


sarah = get_coach_data('sarah2.txt')
mikey = get_coach_data('mikey2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')

sarah_data = into_dict(sarah)
print(sarah_data['nome']+" ("+sarah_data['nasc']+")"", os tempos mais rapidos sao: " +
      str(sorted(set([sanitize(t)for t in sarah]))[0:3]))

mikey_data = into_dict(mikey)
print(mikey_data['nome']+" ("+mikey_data['nasc']+")"", os tempos mais rapidos sao: " +
      str(sorted(set([sanitize(t)for t in mikey]))[0:3]))

julie_data = into_dict(julie)
print(julie_data['nome']+" ("+julie_data['nasc']+")"", os tempos mais rapidos sao: " +
      str(sorted(set([sanitize(t)for t in julie]))[0:3]))

james_data = into_dict(james)
print(james_data['nome']+" ("+james_data['nasc']+")"", os tempos mais rapidos sao: " +
      str(sorted(set([sanitize(t)for t in james]))[0:3]))

# Another way to do the same
# (sarah_name, sarah_date) = sarah.pop(0), sarah.pop(0)
# print(sarah_name+", os tempos mais rapidos sao:" +
#       str(sorted(set([sanitize(t)for t in sarah]))[0:3]))
