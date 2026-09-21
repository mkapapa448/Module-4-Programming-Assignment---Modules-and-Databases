import sqlite3
import csv
import sqlalchemy as sa

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS book
    (title TEXT,
    author TEXT,
    year INTEGER)''')

with open('books2.csv', 'rt') as file:
    reader = csv.reader(file)
    next(reader)
    
    ins = 'INSERT INTO book (title, author, year) VALUES (?, ?, ?)'
    for row in reader:
        cursor.execute(ins, (row[0], row[1], int(row[2])))
    conn.commit()
    conn.close()

engine = sa.create_engine('sqlite:///books.db')
with engine.connect() as connection:
    query = sa.text("SELECT title FROM book ORDER BY title ASC")
    result = connection.execute(query)
    for row in result:
        print(row[0])
