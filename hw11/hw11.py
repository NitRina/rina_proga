import re

def new_text():
    with open('ling.txt', encoding='utf-8') as f:
        text = f.read()   
    a = re.sub(
        r'([^а-я])(язык)((:?а|у|ом|е|и|ов|ам|ами|ах)?)([^а-я])',
        r'\1шашлык\3\5',
        text
    )
    b = re.sub(
        r'(Язык)((:?а|у|ом|е|и|ов|ам|ами|ах)?)([^а-я])',
        r'Шашлык\2\4',
        a
    )
    print(b)
    return b

def main(b):
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(b)
    

if __name__ == "__main__":        
    main(new_text())
