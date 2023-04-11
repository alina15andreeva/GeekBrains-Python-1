s = int(input('Введите сумму: '))
p = int(input('Введите произведение: '))
for x in range (1000):
    if (s - x) + x == s and (s - x)*x == p:
        print(x, s - x)
        break
