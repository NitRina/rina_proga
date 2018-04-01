import re

def choose_university():
    print('Выбирете из списка университет, год основания которого вы хотите узнать\nSynergy\nHSE\nMSU\nMGIMO\nИли добавьте в папку файл с кодом страницы любого, интересующего вас университета')
    file = input('\nВведите название выбранного университета (или имя вашего файла без указания формата): ')
    return file

def main(file):
    with open(file + '.html', encoding='utf-8') as f:
        html = f.read()   
    m = re.search(
        'Год\sоснования</th><td.*?>\n<p><span.*?><a.*?>(\d{4}).*?</a></span>',
        html,
        re.DOTALL
    )
    print('Год основания ' + file + ' - ' + m.groups()[0])
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write('\nГод основания ' + file + ' - ' + m.groups()[0])
        

if __name__ == "__main__":        
    main(choose_university())
