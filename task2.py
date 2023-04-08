n = str(input('Input 3-digit number: '))
if len(n) != 3:
    print('Please, input 3-digit positive number')
else:
    sum = int(n[0]) + int(n[1]) + int(n[2])
    print(sum)