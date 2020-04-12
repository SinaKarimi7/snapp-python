import sqlite3

con = sqlite3.connect(':memory:')

def execute_sql(sql, *parameters):
    cur = con.cursor()
    if parameters:
        cur.execute(sql, parameters)
    else:
        cur.execute(sql)
    con.commit()
def fetch_sql(sql, *parameters):
    cur = con.cursor()
    if parameters:
        cur.execute(sql, parameters)
    else:
        cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    return result

def create_users_table():
    execute_sql(
        'CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, credit INTEGER DEFAULT 0)'
    )
def insert_user(id, name, credit = 0):
    execute_sql(f"INSERT INTO users VALUES (?, ?, ?)", id, name, credit)
def show_users():
    for row in fetch_sql('SELECT * from users'):
        print(row)
def show_user_with_credit(min_credit):
    for row in fetch_sql('SELECT * FROM users WHERE credit >= ?', min_credit):
        print(row)
def update_user_by_id(id, new_credit):
    execute_sql('UPDATE users SET credit=? WHERE id=?', new_credit, id)
def update_user_by_name(name, new_credit):
    execute_sql('UPDATE users SET credit=? WHERE name=?', new_credit, name)
def delete_user_by_id(id):
    execute_sql('DELETE FROM users WHERE id=?', id)

create_users_table()
insert_user(1, 'ali', 1000)
insert_user(2, "meh', 0); DELETE from users", 100)
insert_user(3, 'ziba', 1000)
show_users()

print('---------------')
print('UPDATE[name]')
update_user_by_name('ali', 2000)
show_users()

print('---------------')
print('UPDATE[id]')
update_user_by_id(3, 5000)
show_users()

print('---------------')
print('SELECT[by credit]')
show_user_with_credit(2000)

print('---------------')
print('DELETE[id]')
delete_user_by_id(2)
show_users()