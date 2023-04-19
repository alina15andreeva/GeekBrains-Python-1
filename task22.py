n = int(input('Input the number of elements for list 1: '))
m = int(input('Input the number of elements for list 2: '))
a1 = set()
a2 = set()
for i in range(n):
    x = int(input(f'Input {i+1} element for list 1: '))
    a1.add(x)
for j in range(m):
    y = int(input(f'Input {j+1} element for list 2: '))
    a2.add(y)
print(*sorted(a1.intersection(a2)))
