import csv
import json
import os


result = []
books_whithout_publisher = []

books = open('C:\\Users\\Андрей ПК\\Downloads\\books.csv', newline='')
books_dict = csv.DictReader(books)
books_number = 0
for row in books_dict:
    books_whithout_publisher.append({'title': row['Title'], 'author': row['Author'], 'pages': row['Pages'],
                                     'genre': row['Genre']})
    books_number += 1


users = open('C:\\Users\\Андрей ПК\\Downloads\\users.json', "r")
users_dict = json.load(users)
users_number = 0
for row in users_dict:
    result.append({'name': row['name'], 'gender': row['gender'], 'address': row['address'],
                   'age': row['age'], 'books': []})
    users_number += 1

books_for_users = books_number//users_number  # расчет того, сколько целых книг может получить каждый пользователь
difference = books_number % users_number  # расчет остатка при таком распределении

i = 0  # счетчик пользователей
z = 0  # счетчик книг
for user in result:
    j = 0
    if difference > 0:
        k = 1
    else:
        k = 0
    while j < (books_for_users + k):
        result[i]['books'].append({'title': books_whithout_publisher[z].get('title'),
                                   'author': books_whithout_publisher[z].get('author'),
                                   'pages': books_whithout_publisher[z].get('pages'),
                                   'genre': books_whithout_publisher[z].get('genre')})
        j += 1
        z += 1
    difference -= 1
    i += 1

work_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'result.json'
file_path = os.path.join(work_dir, file_name)

with open(file_path, "w") as f:
    s = json.dumps(result, indent=4)
    f.write(s)

books.close()
users.close()
