import sqlite3

com = sqlite3.connect('sales.db')
cur = con.cursor()

cur.execute('''CREATE TABLE salesmen(
    id_salesmen INT PRIMARY KEY AUTO INCREMENT,
    name WARCHAR);''')
    
cur.execute('''CREATE TABLE customers(
    id_customer INT PRIMARY KEY AUTO INCREMENT,
    name WARCHAR,
    phone INT,
    email WARCHAR
    );''')

cur.execute('''CREATE TABLE sales(
    id INT PRIMARY KEY AUTO INCREMENT,
    name TEXT,
    sum INT NOT NULL
    id_salermen INT,
    id_customer INT
    FOREIGN KEY(id_salermen) REFERENCES salesmen(id_salesmen),
    FOREIGN KEY(id_customer) REFERENCES customers(id_customer)  );''')

con.commit()
con.close()
