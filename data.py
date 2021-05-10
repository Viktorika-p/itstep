import sqlite3

con = sqlite3.connect(test.db)
cur = con.cursor()

cur.execute('''CREATE TABLE peoples(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	last_name TEXT,
    sec_name TEXT,
    city TEXT,
    country TEXT,
    birth INTEGER DATETIME);''')


while True:
    d = input("add last, sec, city, country and birth")
    add = cur.execute(f"INSERT INTO peoples (last_name, sec_name, city, country, birth) VALUES {d};")
    print(add)
else:
    break

con.commit()
con.close()
