# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

n = int(input('Enter the number of elements: '))
a = []
for i in range(n):
    element = int(input(f'Enter {i + 1} element: '))
    a.append(element)
x = int(input('Enter x: '))
min_dist = abs(a[0] - x)
closest = a[0]
for i in a:
    if abs(i - x) < min_dist:
        min_dist = abs(i - x)
        closest = i
print(closest)
