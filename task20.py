word = input('Enter a word: ')
count = 0
d = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'): 1, ('D', 'G'): 2, ('B', 'C', 'M', 'P'): 3, ('F', 'H', 'V', 'W', 'Y'): 4, ('K'): 5,
     ('J', 'X'): 8, ('Q', 'Z'): 10,
     ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'): 1, ('Д', 'К', 'Л', 'М', 'П', 'У'): 2, ('Б', 'Г', 'Ё', 'Ь', 'Я'): 3, ('Й', 'Ы'): 4,
     ('Ж', 'З', 'Х', 'Ц', 'Ч'): 5, ('Ш', 'Э', 'Ю'): 8, ('Ф', 'Щ', 'Ъ'): 10}
for i in word:
    for key, value in d.items():
        for j in key:
            if i.lower() == j.lower():
                count += value
print(count)