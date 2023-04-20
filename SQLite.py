import sqlite3
import datetime 

with sqlite3.connect('D/IT/Github/Projects/Dictionary/database.db') as db:  # db, db3, sqlite, sqlite3
    cursor = db.cursor()
    query1 = """ INSERT INTO expenses (id, name) VALUES(1, 'Комуналка') """
    query2 = """ INSERT INTO expenses (name, id) VALUES('Бензин', 2) """
    query3 = """ INSERT INTO expenses VALUES(3, 'Інтернет') """
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()




def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))


def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


insert_payments = [
    (1, 120, get_timestamp(2020, 9, 1), 1)
    (2, 12, get_timestamp(2020, 9, 1), 3)
    (3, 20, get_timestamp(2020, 9, 1), 2)
    (4, 20, get_timestamp(2020, 9, 2), 2)
    (5, 20, get_timestamp(2020, 9, 3), 2)
]


with sqlite3.connect('D/IT/Github/Projects/Dictionary/database.db') as db:  # db, db3, sqlite, sqlite3
    cursor = db.cursor()
    query = """ INSERT INTO payments(id, amount, payment_date, expense_id)
                            VALUES(?,?,?,?);  """
 
    cursor.executemany(query, insert_payments)
    db.commit()
    print(cursor.rowcount, "Строк добавлено")