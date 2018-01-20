import random

def sub():
    with open('sub.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb():
    with open('verb.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb1():
    with open('verb1.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb2():
    with open('verb2.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def obj():
    with open('obj.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def loc():
    with open('loc.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def time():
    with open('time.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def adj():
    with open('adj.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)    

def a():
    sen1 = adj() + ' ' + sub() + ' ' + time() + ' ' + verb() +\
           ' ' + obj() + ' в ' + loc() + '. '
    sen1 = sen1.capitalize()
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(sen1 + '\n')

def b():
    sen2 = adj() + ' ' + sub() + ' ' + time() + ' не ' + verb() +\
           ' ' + obj() + ' в ' + loc() + '. '
    sen2 = sen2.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(sen2 + '\n')

def c():
    sen3 = verb() + ' ли ' + adj() + ' ' + sub() + ' ' + time() + ' ' +\
           ' ' + obj() + ' в ' + loc() + '? '
    sen3 = sen3.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(sen3 + '\n')

def d():
    sen4 = time() + ' ' + verb1() + ' ' + obj() + ' в ' +\
           loc() + ', ' + adj() + ' ' + sub() + '! '
    sen4 = sen4.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(sen4 + '\n')

def e():
    sen5 = adj() + ' ' + sub() + ' ' + verb2() + ' бы ' +\
           obj() + ' в ' + loc() + '. '
    sen5 = sen5.capitalize()
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(sen5)

def text():
    a()
    b()
    c()
    d()
    e()
    
    with open('text.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        random.shuffle(word)
        result = ''.join(word)
        print(result)

text()

