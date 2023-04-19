n = int(input('Input the number of bushes: '))
a = []
berries = []
for i in range(n):
    x = int(input(f'Input the number of berries per bush {i+1}: '))
    a.append(x)
for j in range(len(a) - 1):
    count = a[j-1] + a[j] + a[j+1]
    berries.append(count)
    count = 0
else:
    count = a[-1] + a[-2] + a[0]
    berries.append(count)
print(max(berries))