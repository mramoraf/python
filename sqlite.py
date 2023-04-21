import sqlite3
from random import randint

global db
global sql

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")


db.commit()


def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute('INSERT INTO users VALUES (?,?,?)', (user_login, user_password, 0))
        db.commit()

        print('Successfully registered! ')
    else:
        print('This information already exists')
  
        for value in sql.execute('SELECT * FROM users'):
            print(value)



def delete_db():
    sql.execute(f'DELETE FROM users WHERE login  = "{user_login}"')
    db.commit()
 
    print('Account deleted')




def casino():
    global user_login
    user_login = input('Log in: ')
    number = randint(1,2)


    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('This login doesnt exist. Lets register!')
        reg()
    else:
        sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
        for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}"):
            balance = i[0]
        if number == 1:
            sql.execute(f'UPDATE users SET cash = {1000 + balance} WHERE login = "{user_login}"')
            db.commit()
        else:
            print('You lost!')
            delete_db()


def enter():
    for i in sql.execute('SELECT login, cash FROM users'):
        print(i)


def main ():
    casino()
    enter()

main()



























