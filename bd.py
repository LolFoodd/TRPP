import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS 'employees' (
	'id' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'position' TEXT
)
""")

cur.execute("INSERT INTO 'employees' ('name', 'email', 'phone_number', 'position')  VALUES (?, ?, ?, ?)",
            ('Иванова Татьяна Жолобовна', 'zxc@gmail.com', '+79651234321', 'Массажист'))

cur.execute("INSERT INTO 'employees' ('name', 'email', 'phone_number', 'position')  VALUES (?, ?, ?, ?)",
            ('Сидорова Раиса Витальевна', 'qwerty@gmail.com', '+79256781234', 'Уборщица'))
cur.execute("INSERT INTO 'employees' ('name', 'email', 'phone_number', 'position')  VALUES (?, ?, ?, ?)",
            ('Твердохлеб Поэтресс Устинович', 'mshkamsk@gmail.com', '+71116781234', 'Менеджер'))

cur.execute("""CREATE TABLE IF NOT EXISTS 'clients' (
	'id' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT
);
""")

cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number')  VALUES (?, ?, ?)",
            ('Петренко Авдотья Викторовна', 'asd@gmail.com', '+79094321567'))
cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number')  VALUES (?, ?, ?)",
            ('Фролова Марина Станиславовна', 'kek@gmail.com', '+78005553535'))
cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number')  VALUES (?, ?, ?)",
            ('Технов Диджитал Данович', 'lol@gmail.com', '+74565553535'))


cur.execute("""CREATE TABLE IF NOT EXISTS 'contracts' (
	'id' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'services_type_id' INTEGER,
	'start_price' INTEGER,
	'discount' INTEGER,
	'finish_price' INTEGER,
	'client_id' INTEGER,
	'employee_id' INTEGER
)
""")

cur.execute("INSERT INTO 'contracts' ('number', 'date', 'services_type_id', 'start_price', 'discount', 'finish_price', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('143', '2020-05-30', 1, 1000, 10, 900, 1, 1))
cur.execute("INSERT INTO 'contracts' ('number', 'date', 'services_type_id', 'start_price', 'discount', 'finish_price', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('143', '2021-05-30', 2, 2000, 10, 1800, 1, 1))
cur.execute("INSERT INTO 'contracts' ('number', 'date', 'services_type_id', 'start_price', 'discount', 'finish_price', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ('143', '2022-05-30', 3, 1000, 20, 800, 1, 1))

cur.execute("""CREATE TABLE IF NOT EXISTS 'type_services' (
	'id' INTEGER PRIMARY KEY AUTOINCREMENT,
	'service' TEXT
)
""")

cur.execute("INSERT INTO 'type_services' ('service')  VALUES (?)",
            ('Массаж',))

cur.execute("INSERT INTO 'type_services' ('service')  VALUES (?)",
            ('Педикюр',))

cur.execute("INSERT INTO 'type_services' ('service')  VALUES (?)",
            ('Маникюр',))

connection.commit()
connection.close()
