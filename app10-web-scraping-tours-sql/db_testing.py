import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM Events")
rows = cursor.fetchall()
print(rows)

new_rows = [('Dogs', 'Dog City', '2099.10.17')]
cursor.executemany("INSERT INTO Events (Band, City, Date) VALUES (?,?,?)", new_rows)
connection.commit()