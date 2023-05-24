import view
import database

def main():
    while True:
        ask = view.user_input()
        if ask == 1:
            str = view.add_man()
            database.add_data(str)
        if ask == 2:
            str = view.search_man()
            database.search_data(str)
        if ask == 3:
            database.sort_data_name()
        if ask == 4:
            database.sort_data_bday()
        if ask == 5:
            database.print_name()
        if ask == 6:
            database.print_database()
        if ask == 7:
            database.change_database()
        if ask == 8:
            database.delete_database()
        elif ask == 9:
            break

main()