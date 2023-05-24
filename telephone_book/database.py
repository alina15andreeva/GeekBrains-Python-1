import view

def add_data(data):
    with open('database.txt', 'a') as file:
        file.writelines(data)
        file.write('\n')
    print('Телефонная книга обновлена\n')

def search_data(name):
    with open('database.txt', 'r') as file:
        data = file.readlines()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True
        if flag == False:
            print('Пользователь с такими данными не найден\n')

def sort_data_name():
    with open('database.txt', 'r') as file:
        data = file.readlines()
        data.sort()
    with open('database.txt', 'w') as file:
        file.writelines(data)

def sort_data_bday():
    with open('database.txt', 'r') as file:
        data = file.readlines()
        temp = []
        for i in data:
            temp.append(i.split(';'))
        temp.sort(key = lambda x: x[3])
        temp2 = []
        for i in temp:
            for j in i[0:-1]:
                st = ''.join(j) + ';'
                temp2.append(st)
            temp2.append('\n')
    with open('database.txt', 'w') as file:
        file.writelines(temp2)

def print_name():
    with open('database.txt', 'r') as file:
        data = file.readlines()
        for i in data:
            print(i.split(';')[0])

def print_database():
    with open('database.txt', 'r') as file:
        print(file.read())

def change_database():
    print_database()
    str = int(input('Какую строку вы хотите изменить? '))
    with open('database.txt', 'r') as file:
        data = file.readlines()
        data.pop(str-1)
        new_user = view.add_man() + '\n'
        data.append(new_user)
    with open('database.txt', 'w') as file:
        file.writelines(data)
    print('Телефонная книга обновлена\n')

def delete_database():
    print_database()
    str = int(input('Какую строку вы хотите удалить? '))
    with open('database.txt', 'r') as file:
        data = file.readlines()
        data.pop(str-1)
    with open('database.txt', 'w') as file:
        file.writelines(data)
    print('Телефонная книга обновлена\n')