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

d = input("add last, sec, city, country and birth")
print(d)

while True:
    add = cur.execute("INSERT INTO peoples (last_name, sec_name, city, country, birth) VALUES (d);")
    print(add)
else:
    print("error")

con.commit()
con.close()
