def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return power(a, b-1) * a
a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(power(a, b))