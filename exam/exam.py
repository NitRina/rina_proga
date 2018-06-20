import re
import os
import collections

def task_1(path):
    files = [files for root, dirs, files in os.walk(path)]
    a = files[0]
    for file in a :
        if file == '.DS_Store':
            continue
        f_name = file.strip('.html') + '.txt'
        with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
            text = f.read()
            text = text.replace('`', '')
            cleanr = re.compile('<.*?>')
            n_text = re.sub(cleanr, '', text)
            with open(f_name, 'w', encoding='cp1251') as f:
                f.write(n_text)
                
def task_2(path):
    files = [files for root, dirs, files in os.walk(path)]
    a = files[0]
    for file in a :
        if file == '.DS_Store':
            continue
        d = {}
        names = re.findall(r'</ana>{[А-ЯЁ].*?}</w>', a)
        print(names)
        for name in names:
            d[name] = len(name)

    
    
task_1('news')
task_2('news')

