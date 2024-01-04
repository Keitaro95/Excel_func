import sqlite3

#全部のレコードを返す関数
def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

#１つのデータをテーブルに追加する関数
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()

#IDでレコードを削除する関数
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

#複数データをテーブルに追加する
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

#emailを検索する
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


