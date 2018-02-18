import random

def get_dict1():
    d = {}
    with open('words.csv', encoding='utf-8') as f:
        for line in f:
            word = line.strip().split(',')
            d[word[1]] = word[0]
    return d

def get_dict2():
    d = {}
    with open('words.csv', encoding='utf-8') as f:
        for line in f:
            word = line.strip().split(',')
            d[word[3]] = word[2]
    return d

def get_puzzle1(d):
    puzzle = random.choice(list(d.keys()))
    answer = len(puzzle)
    print('------SUPER-GAME------\n\nВ фразеологизме из мифов Древней Греции пропущенное слово заменено троеточием.\nВам нужно угадать, какое слово было пропущено.\nОтвет вводите с маленькой буквы в той форме, в которой слово должно стоять (но не забывайте заглавные буквы в именах собственных).\nУ вас будет столько попыток, сколько слов в пропущенном слове.\nУдачи!\n\n', d[puzzle], ' ...\n')
    for i in range(len(puzzle)):
        idea = input('Введите недостающее слово: ')
        if idea == puzzle:
            print('Всё верно! Вижу, вы знакомы с мифами Древней Греции с:\n')
            break
        else:
            answer += -1
            print('Что-то не то, попробуйте снова.\n')
    if answer == 0:
        print('Попытки закончились.\nПравильный ответ: ', d[puzzle], puzzle,'\nМожете погуглить значение этого фразеологизма, а лучше почитайте мифы.\n\n')

def get_puzzle2(d):
    puzzle = random.choice(list(d.keys()))
    answer = len(puzzle)
    print('------SUPER-GAME------\n\nВ фразеологизме из мифов Древней Греции пропущенное слово заменено троеточием.\nВам нужно угадать, какое слово было пропущено.\nОтвет вводите с маленькой буквы в той форме, в которой слово должно стоять (но не забывайте заглавные буквы в именах собственных).\nУ вас будет столько попыток, сколько слов в пропущенном слове.\nУдачи!\n\n... ', d[puzzle], '\n')

    for i in range(len(puzzle)):
        idea = input('Введите недостающее слово: ')
        if idea == puzzle:
            print('Всё верно! Вижу, вы знакомы с мифами Древней Греции с:\n')
            break
        else:
            answer += -1
            print('Что-то не то, попробуйте снова.\n')
    if answer == 0:
        print('Попытки закончились.\nПравильный ответ: ', puzzle, d[puzzle],'\nМожете погуглить значение этого фразеологизма, а лучше почитайте мифы.\n\n')

def main():
        a = random.choice([1,2])
        if a == 1:
            d = get_dict1()
            get_puzzle1(d)
        else:
            d = get_dict2()
            get_puzzle2(d)
        main()

if __name__ == '__main__':
    main()
