words1=0
words3=0

with open("text.txt", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        for i in words:
                if len(i) == 3:
                words3 =+1
            elif len(i) == 1:
                words1 =+1
if words_1 == 0:
    print("Нет слов длины 1")
elif words_3 == 0:
    print("Нет слов длины 3")
else:
    print("Слов длины 3 в", words3 / words1, "раз больше, чем слов длины 1")
