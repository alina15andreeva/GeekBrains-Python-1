n = int(input('Введите кол-во чисел: '))
a = [int(input(f'Введите число {i+1}: ')) for i in range(n)]
b = [int(input(f'Введите число {i+1}: ')) for i in range(2)]
index = []
for j in range(len(a)):
    if b[0] <= a[j] <= b[1]:
        index.append(j)
print(index)