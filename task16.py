#  Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

n = int(input('Enter the number of elements: '))
a = []
for i in range(n):
    element = int(input(f'Enter {i + 1} element: '))
    a.append(element)
x = int(input('Enter x: '))
print(a.count(x))