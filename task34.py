phrase = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.split(' ')
check = list(map(lambda x: x.count('а') + x.count('о') + x.count('у') + x.count('э') + + x.count('ы') + + x.count('я') + x.count('ё')
                 + x.count('е') + x.count('ю') + x.count('и'), phrase))
if len(set(check)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')