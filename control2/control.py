import re

def count_lines():
    with open('mystem.xml', encoding='utf-8') as f:
        text = f.read()   
    a = re.findall(
        r'<w><ana\slex=.*?</w>',
        text,
        re.DOTALL
    )
    with open('text1.txt', 'w', encoding='utf-8') as f:
        f.write(str(len(a)))
    return text

def make_dict(text):
    d = {}
    words = re.findall('gr="(.*?)"', text)
    for words in text:
        if words in d:
            d[words] += 1
        else:
            d[words] = 1
    return d

def main(d):
    print(d)

    

if __name__ == "__main__":        
    main(make_dict(count_lines()))



