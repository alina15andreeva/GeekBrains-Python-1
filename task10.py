n = int(input('Кол-во монеток: '))
zero_count = 0
one_count = 0 
for i in range(n):
    moneta = int(input('Введите 0 или 1: '))
    if moneta == 0:
        zero_count += 1
    else:
        one_count += 1
if zero_count < one_count:
    print(zero_count)
else:
    print(one_count)