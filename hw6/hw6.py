import random

def sub_m():
    with open('sub_m.txt',encoding='utf-8') as f:       
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def sub_f():
    with open('sub_f.txt',encoding='utf-8') as f:       
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def sub_pl():
    with open('sub_pl.txt',encoding='utf-8') as f:       
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb_pr_s():
    with open('verb_pr_s.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb_pr_pl():
    with open('verb_pr_pl.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb_imp():
    with open('verb_imp.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def verb_past():
    with open('verb_past.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def if_verb_m():
    with open('if_verb_m.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def if_verb_f():
    with open('if_verb_f.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def if_verb_pl():
    with open('if_verb_pl.txt',encoding='utf-8') as f:
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

def question():
    with open('question.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def adj_m():
    with open('adj_m.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)    

def adj_f():
    with open('adj_f.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word)

def adj_pl():
    with open('adj_pl.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        return random.choice(word) 

def a1():
    sen = adj_m() + ' ' + sub_m() + ' ' + time() + ' ' +\
           verb_pr_s() + ' ' + obj() + ' в ' + loc() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'w', encoding='utf-8') as f:
        f.write(sen + '\n')

def a2():
    sen = adj_f() + ' ' + sub_f() + ' ' + time() + ' ' +\
           verb_pr_s() + ' ' + obj() + ' в ' + loc() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'w', encoding='utf-8') as f:
        f.write(sen + '\n')

def a3():
    sen = adj_pl() + ' ' + sub_pl() + ' ' + time() + ' ' +\
           verb_pr_pl() + ' ' + obj() + ' в ' + loc() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'w', encoding='utf-8') as f:
        f.write(sen + '\n')

def b1():
    sen = adj_m() + ' ' + sub_m() + ' ' + time() + ' не ' +\
           verb_pr_s() + ' ' + obj() + ' в ' + loc() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def b2():
    sen = adj_f() + ' ' + sub_f() + ' ' + time() + ' не ' +\
           verb_pr_s() + ' ' + obj() + ' в ' + loc() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def b3():
    sen = adj_pl() + ' ' + sub_pl() + ' ' + time() + ' не ' +\
           verb_pr_pl() + ' ' + obj() + ' в ' + loc() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def c1():
    sen = verb_pr_s() + ' ли ' + adj_m() + ' ' + sub_m() + ' ' +\
           time() + ' ' + ' ' + obj() + ' в ' + loc() + '? '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def c2():
    sen = verb_pr_s() + ' ли ' + adj_f() + ' ' + sub_f() + ' ' +\
           time() + ' ' + ' ' + obj() + ' в ' + loc() + '? '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def c3():
    sen = verb_pr_pl() + ' ли ' + adj_pl() + ' ' + sub_pl() + ' ' +\
           time() + ' ' + ' ' + obj() + ' в ' + loc() + '? '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def c4():
    sen = question() + adj_m() + ' ' + sub_m() + ' ' + time() +\
           ' ' + verb_pr_s() + ' ' + obj() + ' в ' + loc() + '? '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def c5():
    sen = question() + adj_f() + ' ' + sub_f() + ' ' + time() +\
           ' ' + verb_pr_s() + ' ' + obj() + ' в ' + loc() + '? '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def c6():
    sen = question() + adj_pl() + ' ' + sub_pl() + ' ' + time() +\
           ' ' + verb_pr_pl() + ' ' + obj() + ' в ' + loc() + '? '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def d1():
    sen = time() + ' ' + verb_imp() + ' ' + obj() + ' в ' +\
           loc() + ', ' + adj_m() + ' ' + sub_m() + '! '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def d2():
    sen = time() + ' ' + verb_imp() + ' ' + obj() + ' в ' +\
           loc() + ', ' + adj_f() + ' ' + sub_f() + '! '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def d3():
    sen = time() + ' ' + verb_imp() + 'те ' + obj() + ' в ' +\
           loc() + ', ' + adj_pl() + ' ' + sub_pl() + '! '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen + '\n')

def e1():
    sen = adj_m() + ' ' + sub_m() + ' ' + verb_past() + ' бы ' +\
           obj() + ' в ' + loc() + ', если бы ' + if_verb_m() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen)
        
def e2():
    sen = adj_f() + ' ' + sub_f() + ' ' + verb_past() + 'a бы ' +\
           obj() + ' в ' + loc() + ', если бы ' + if_verb_f() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen)

def e3():
    sen = adj_pl() + ' ' + sub_pl() + ' ' + verb_past() + 'и бы ' +\
           obj() + ' в ' + loc() + ', если бы ' + if_verb_pl() + '. '
    sen = sen.capitalize()
    with open('text1.txt', 'a', encoding='utf-8') as f:
        f.write(sen)

def text1():
    
    centense1 = random.choice([1,2,3])
    if centense1 == 1:
        a1()
    elif centense1 == 2:
        a2()
    else:
        a3()
        
    centense2 = random.choice([1,2,3])
    if centense2 == 1:
        b1()
    elif centense2 == 2:
        b2()
    else:
        b3()
        
    centense3 = random.choice([1,2,3,4,5,6])
    if centense3 == 1:
        c1()
    elif centense3 == 2:
        c2()
    elif centense3 == 3:
        c3()
    elif centense3 == 4:
        c4()
    elif centense3 == 5:
        c5()
    else:
        c6()
        
    centense4 = random.choice([1,2,3])
    if centense4 == 1:
        d1()
    elif centense4 == 2:
        d2()
    else:
        d3()

    centense5 = random.choice([1,2,3])
    if centense5 == 1:
        e1()
    elif centense5 == 2:
        e2()
    else:
        e3()
    
    with open('text1.txt',encoding='utf-8') as f:
        words = f.read()
        word = words.split('\n')
        random.shuffle(word)
        result = ''.join(word)
        print(result)

text1()
