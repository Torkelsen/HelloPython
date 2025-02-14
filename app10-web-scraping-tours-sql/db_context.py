import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM Events")
rows = cursor.fetchall()
print(rows)

new_rows = [('Cats', 'Cat City', '2088.10.17')]
print(new_rows)
cursor.executemany("INSERT INTO Events (Band, City, Date) VALUES (?,?,?)", new_rows)
connection.commit()

