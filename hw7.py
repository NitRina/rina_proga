import collections

def find_file():
 #   fname = input('Введите имя файла в формате имя_фала.txt: ')
    try:
        f = open(fname)
    except IOError as e:
        print("Файл не найден. Попробуйте ещё раз.")
        find_file()
    else:
        all_words(fname)

def all_words(fname): 
    with open(fname, encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    symbols = ''',.:;()-?!*'"\|/[]}{«»@#$%~`^&'''
    for s in symbols:
        text = text.replace(s,'')
    words = text.split()
    return words

def all_hoods(words):
    d = {}
    for word in words:
        if word.endswith('hood') and word != 'hood':
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d

def count_hoods(d):
    keys = list(d.keys())
    if len(keys) > 0:
        print('В тексте' + str(len(keys)) + 'сущ. с суффиксом -hood')
        words = sorted(d, key = d.get)
        print('Наименее частотное слово с суффиксом hood - ' + words[0])
        for k in sorted(d, key = d.get, reverse = True):
            motives += [k[:len(k)-4]]
        print('Основы:' + motives)
        
    else:
        print('В тексте нет существительных с суффиксом -hood.')


fname = input('Введите имя файла в формате имя_фала.txt: ')
find_file()
words = all_words(fname)
d = all_hoods(words)
count_hoods(d)
