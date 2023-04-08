n = str(input('Input 6-digit number: '))
if len(n) != 6:
    print('Please, input 6-digit positive number')
else:
    if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
        print('Yes')
    else:
        print('No')