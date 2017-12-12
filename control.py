

with open("Extinct_languages.txt", encoding="utf-8") as f:
    lines = f.readlines()

    
    for line in lines:
        if len(line) > 35:
            print(line)

    x = 0
    for line in lines:        
        y = 'Critically endangered'
        if y in line:
            x += 1
    print(x)


    c = ''
    for line in lines:
        z = line
        a = input('Введите название языка: ')
        while a:
            if a in z:
                c += z
                a = input('Введите название языка: ')


        print(c)
                

                
                    


