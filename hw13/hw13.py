import os
import collections

def make_dict():
    extention = []
    for root, dirs, files in os.walk('.'):
        for fl in files:
            filename, element = os.path.splitext(fl)
            extention.append(element)
    return extention

def most_common_ext(extention):
    counter = collections.Counter(collections.Counter(extention)).most_common(1)[0][0]
    return counter

print('Чаще всего встречается разрешение: ', most_common_ext(make_dict()))
    

