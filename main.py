from functions import *
phone_book_file = 'data/users.json'
new_book_file = 'data/new_book.json'

def menu():
    print("1. Загрузить телефонную книгу")
    print("2. Сохранить изменения в телефонной книге")
    print("3. Показать все контакты")
    print("4. Создать контакт")
    print("5. Удалить контакт")
    print("6. Поиск по ФИО, Компании, Комментарию, ID")
    print("7. Выйти из программы")

def main():
    is_phonebook_loaded = False
    phone_book = None
    is_phonebook_changed = False
    while True:
        menu()
        ask = input("Выберите нужный пункт меню и нажмите Ввод: ")
        print()
        if ask == '1': #Загрузка телефонной книги
            phone_book = load_phonebook(phone_book_file)
            is_phonebook_loaded = True
            print("Телефонная книга загружена")
        elif ask == '2': #Сохранение
            if not phone_book:
                phone_book = load_phonebook(phone_book_file)
            save_phonebook(new_book_file, phone_book)
            print("Телефонная книга сохранена")
        elif ask == '3':  # Распечатка телефонной книги
            if not is_phonebook_loaded:
                print("Телефонная книга не загружена!")
            else:
                show_all_contacts(phone_book)
        elif ask == '4': #Создание абонента
            user_id = generate_userid()
            while user_id in phone_book.keys():
                user_id = generate_userid()
            username = input("Введите ФИО абонента: ")
            phone = input("Введите телефон абонента: ")
            company = input("Введите компанию: ")
            comment = input("Введите комментарий (не обязательно): ")
            if username and phone and company:
                phone_book[user_id] = {"ФИО" : username,
                                       "Телефон": phone,
                                        "Компания": company,
                                        "Комментарии": comment}
                is_phonebook_changed = True
            else:
                print("Не все данные указаны!")
        elif ask == '5':
            if not is_phonebook_loaded:
                print("Телефонная книга не загружена!")
            else:
                id_to_delete = input("Введите ID абонента: ")
                if id_to_delete in phone_book:
                    phone_book.pop(id_to_delete)
                    print("Абонент удален из телефонной книги")
                else:
                    print("Указанный ID не найден")
            is_phonebook_changed = True
        elif ask == '6':
            if not is_phonebook_loaded:
                print("Телефонная книга не загружена!")
            else:
                searchstr = input("Введите любое поле для поиска: ").strip()
                result = find_by_any(phone_book, searchstr)
        elif ask == '7':
            if is_phonebook_changed:
                print("В телефонную книгу был внесены изменения")
                ask = ''
                while ask not in ("Y", "N"):
                    ask = input("Применить изменения (запись в файл) ? Y/N: ")
                    if ask == 'Y':
                        data = json.dumps(phone_book, indent=4, ensure_ascii=False)
                        with open(new_book_file, 'w', encoding='utf-8') as file:
                            file.write(str(data))
                    elif ask == 'N':
                        pass
                    else:
                        print("Неверно, повторите ввод.")
            print("Выходим из программы...")
            break
        else:
            print("Выбор неверен, повторите ввод")

if __name__ == '__main__':
    main()
