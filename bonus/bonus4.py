x = input('Введите текст на русском:')
for z in 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я':
    x = x.replace(z,z+'с'+z)
for z in 'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я':
    x = x.replace(z,z+'с'+z.lower())    
print ('Перевод на кирпичный язык:', x)

    