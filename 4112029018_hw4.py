import sqlite3

conn=sqlite3.connect('BBQ.db')
cursor=conn.cursor()
cursor.execute('''
  CREATE TABLE IF NOT EXISTS meats(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    quantity INTEGER
  )''')


cursor.execute("INSERT INTO meats(name, price, quantity) VALUES('chicken', 30, 5)")
cursor.execute("INSERT INTO meats(name, price, quantity) VALUES('beaf', 55, 10)")
cursor.execute("INSERT INTO meats(name, price, quantity) VALUES('pork', 40, 15)")
conn.commit()

cursor.execute("UPDATE meats SET price=35 WHERE name='pork'")
cursor.execute("UPDATE meats SET quantity=30 WHERE name='chicken'")
conn.commit()

cursor.execute("DELETE FROM meats WHERE price=40")
conn.commit()

cursor.execute("SELECT*FROM meats")
meats=cursor.fetchall()

print("烤肉列表:")
for meat in meats:
    print(meat)

cursor.close()
conn.close()