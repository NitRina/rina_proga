a = 0
with open('text.txt', 'w', encoding='utf-8') as f:
    b = input('Введите слово: ')
    while b:
        a += 1
        b = b[a::1]
        f.write(b + '\n')
        b = input('Введите слово: ')

#проверка         
with open("text.txt", encoding="utf-8") as f:
    c = f.read()
print('В файл записано: ', c)
