n = int(input('Input n: '))
m = int(input('Input m: '))
k = int(input('Input k: '))
if k <= n * m and (k % n == 0 or k % m == 0):
    print('Yes')
else:
    print('No')