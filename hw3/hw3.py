a = input('Введите слово: ')
while a:
    print(a)
    for i in range(0, len(a)-1):
        b = []
        b.append(a[1:len(a):1])
        s1 = aабракадабра[:1]
        b.append(s1)
        s2 = "".join(b)
        print(s2)
        a = s2
    a = input("Введите слово: ")
