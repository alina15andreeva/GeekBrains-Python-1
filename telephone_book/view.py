def user_input():
    ask = int(input("Выбери ниже\n 1 - Записать пользователя в телефонную книжку\n 2 - Поиск по данным\n 3 - Отсортировать справочник по имени\n 4 - Отсортировать справочник по дате рождения\n 5 - Вывод только имён абонентов\n 6 - Вывод справочника\n 7 - Изменить данные абонента\n 8 - Удалить абонента\n 9 - Выход\n Ваш выбор: "))
    return ask

def add_man():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    middle = input('Введите отчество: ')
    birthdate = input('Введите дату рождения: ')
    phone = input('Введите номер телефона: ')
    man = name + '; ' + surname + '; ' + middle + '; ' + birthdate + '; ' + phone + '; '
    return man

def search_man():
    str_search = input('Введите строку для поиска: ')
    return str_search