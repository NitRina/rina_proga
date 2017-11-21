l1 = 0
l3 = 0

with open('text.txt', encoding='utf-8') as f:
    text = f.read()
    text = text.replace ('.', '')
    text = text.replace (',', '')
    text = text.replace (':', '')
    text = text.replace (';', '')
    text = text.replace ('!', '')
    text = text.replace ('—', '')
    text = text.replace ('«', '')
    text = text.replace ('»', '')
    text = text.replace ('?', '')
    text = text.replace ('…', '')
    text1 = text.split()
    for i in text1:
        if len(i) == 3:
            l3 += 1
        elif len(i) == 1:
            l1 += 1
if l1 == 0:
    print('Нет слов длины 1')
else:
    print('Слов длины 3 в', l3 / l1, 'раз больше, чем слов длины 1')

#слова с дефисом я считаю за единое слово, дефис тоже считается за отдельный символ в его длине
