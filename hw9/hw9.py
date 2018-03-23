import re

def open_f():
    file = input('Введите имя файла ')
    with open(file, encoding='utf-8') as f:
        symbols = ''',.:;()-?!*'"\|/[]}{«»@#$%~`^&'''
        words = f.read()
        for s in symbols:
            words = words.replace(s,'')
        words = words.lower().split()
        return words

def find(words):
    prog_f = []
    for word in words:
        if re.match('(?:буд(?:ут?|е(?:шь|м|те?)))?программир(?:у(:?ю(:?т|щ(:?ую|ая|и(:?й|ми?|е|х)|е(:?ю|го|му?|е|й)))?|я|е(:?шь|те?|м(:?ы(:?й|ми?|е|х)?|о(:?го|му?|е|й|ю)?|ая?|ую)?)|й(:?те)?)|ова(:?ть|л(:?а|и)?|в(:?ш(:?ую|ая|и(:?й|ми?|е|х)?|е(:?ю|го|му?|е|й)))?))(?:сь|ся)?$', word) and word not in prog_f:
            prog_f.append(word)
    return prog_f

def main(prog_f):
    print('Найденые формы глагола программировать:')
    for word in prog_f:
        print(word)

if __name__ == "__main__":        
    print(main(find(open_f())))
    
