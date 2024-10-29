import json
from plistlib import dumps
from uuid import uuid4

def load_phonebook(phone_book_file):
    with open(phone_book_file, 'r', encoding='utf-8') as file:
        phone_book_dict = file.read()
    return json.loads(phone_book_dict)

def check_phonebook_is_loaded(phone_book_dict):
    return phone_book_dict

def save_phonebook(new_book_file, phone_book):
    data = json.dumps(phone_book, indent=4, ensure_ascii=False)
    with open(new_book_file, 'w', encoding='utf-8') as file:
        file.write(str(data))

def show_all_contacts(phone_book):
    for k, v in phone_book.items():
        print(f'ID: {k}')
        for k, v in v.items():
            print(f'{k}: {v}')
        print()

def create_contact():
    pass

def find_by_any(phone_book, searchstr):
    #for k, v in phone_book.items():
    print()
    if searchstr in phone_book.keys(): #Поиск по ID
        print()
        print(f'ID: {searchstr}')
        for k, v in phone_book[searchstr].items():
            print(f'{k}: {v}')
        print()
    else:
        print()
        for k, v in phone_book.items():
            if isinstance(v, dict):
                for kk, vv in v.items():
                    if searchstr in vv:
                        print(f'ID: {k}')
                        for k, v in v.items():
                            print(f'{k}: {v}')
                        print()

def generate_userid():
    return str(uuid4())[-12:]