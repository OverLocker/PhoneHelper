from random import choice
from uuid import uuid4
import ujson as json

users = {}

users_file = "data/usernames.txt"
comments_file = "data/comments.txt"
companies_file = "data/companies.txt"

first_phone_octet = [int(i) for i in range(100, 1000)]
phone_octets = [int(i) for i in range(10, 100)]
phone_prefixes = ['903', '916', '919', '993', '985', '499', '495', '940', '912']

def get_user_comment(comments_file=comments_file):
    with open(comments_file, 'r') as file:
        data = file.read().strip().split()
    return choice(data)

def generate_phone_number(phone_prefixes=phone_prefixes, first_octet=first_phone_octet, octets=phone_octets):
    prefix = choice(phone_prefixes)
    first_octet = choice(first_octet)
    return f'+{7}({prefix}){first_octet}-{choice(octets)}-{choice(octets)}'

def generate_username(users_file=users_file):
    with open(users_file, 'r') as file:
        users = file.read().strip().split('\n')
    return choice(users)

def get_users_count(user_file=users_file):
    with open(users_file, 'r') as file:
        users = file.read().strip().split('\n')
    return len(users)

def generate_company(companies_file = companies_file):
    with (open (companies_file, 'r') as companies):
        companies = companies.read().strip().split("\n")
        return choice(companies)

def generate_userid():
    return str(uuid4())[-12:]

def generate_all_users():
    for _ in range(get_users_count()+1):
        user_id = generate_userid()
        if user_id in users.keys():
            print(f'Абонент с указанным {user_id} уже существует!')
            break
        user_name = generate_username()
        user_phone_number = generate_phone_number()
        user_comment = get_user_comment()
        user_company = generate_company()
        users[user_id] = {'ФИО': user_name,
                          'Телефон': user_phone_number,
                          'Компания': user_company,
                          'Комментарии': user_comment}
    return users

def write_json_file(users = users, json_file = 'data/users.json'):
    generate_all_users()
    with open(json_file, 'w', encoding='utf-8') as file:
        dump = json.dumps(users, ensure_ascii=False, indent=4, escape_forward_slashes=False)
        file.write(dump)

write_json_file()