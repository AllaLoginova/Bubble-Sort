n = int(input())   # длина списка
lst = list(map(int, input().split()))

flag = True
res = 0   # общее количество перестановок

while flag:
    count = 0  # количество перестановок за 1 проход по списку
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            count += 1
    if count > 0:   # если была хотя бы 1 перестановка
        n -= 1
        res += count
    else:
        flag = False # выходим из цикла

print(*lst) # отсортированный список
print(res) # общее количество перестановок
------------------------------------------------------
******************************************************
------------------------------------------------------
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)

    def get_user(self, name, password):
        with self.connection as connection:
            cursor = connection.cursor()
            rows = cursor.execute('select * from user where name = ? and password = ?', (name, password))
            res = rows.fetchone()

            return res


    def get_task_by_id(self, task_id, user_id):
        with self.connection as connection:
            cursor = connection.cursor()
            rows = cursor.execute('select * from task where id = ? and user_id = ?', (task_id, user_id))
            res = rows.fetchone()

            return res

    def get_tasks(self, user_id):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute('select * from task where user_id = ?', (user_id, ))
            rows = cursor.fetchall()

            return rows

    def add_task(self, name, user_id):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute('insert into task (name, status, user_id) values (?, ?, ?)', (name, 'сделать', user_id))

    def delete_tasks(self, task_id):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute('delete from task where id = ?', (task_id, ))

    def update_tasks(self, task_id):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute("update todo  set status = 'сделано' where id = ?", (task_id,))

    def __del__(self):
        print('Заканчиваю работу с базой')
        self.connection.close()


class User:
    def __init__(self, name, password, db):
        self.name = name
        self.password = password
        self.db = db

    def auth(self):
        user = self.db.get_user(self.name, self.password)
        if user:
            return user[0]
        return None


db = Database('C:\\Users\\Б - 6\\Documents\\Логинова Алла\\Python\\Занятие 77-78\\todo.db')
emoji = {'сделать': ' 🔴', 'сделано': ' 🟢'}

name = input('Введи имя: ')
password = input('Введи пароль: ')


auth = False

user_id = User(name, password, db).auth()

if user_id:
    auth = True
    print('Авторизация успевшна')
else:
    print('Неверный логин или пароль')


while True and auth:
    print('Что хотите сделать?')
    print('1 - прочитать задачи')
    print('2 - добавить задачу')
    print('3 - удалить задачу')
    print('q')

    res = input('Введи номер: ')

    if res == '1':
        rows = db.get_tasks(user_id)
        print('\n Вот список задач')
        for row in rows:
            task_str = f'{row[0]}. {row[1]} - {row[2]}{emoji[row[2]]}'
            print(task_str)
        print('\n')

    if res == '2':
        name = input('Введи название задачи ')
        db.add_task(name, user_id)
        print('Задача добавлена')

    if res == '3':
        task_id = input('Введи номер задачи')
        task = db.get_task_by_id(task_id, user_id)
        if task:
            db.delete_tasks(task_id, user_id)
            print('Задача удалена 😃')
        else:
            print('Такой задачи нет')


    if res == 'q':
        break

