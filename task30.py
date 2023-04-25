a1 = int(input('Введите первое число: '))
d = int(input('Введите разность: '))
n = int(input('Введите кол-во чисел: '))
a = [a1]
for i in range(2, n + 1):
    a.append(a[0] + (i-1) * d)
print(*a)