import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
''')

cur.execute('DELETE FROM Ages ')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Swarnalakshmi", 33) ')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Natividad", 25) ')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Erika", 21) ')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Erdehan", 33) ')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Kerrie", 21) ')

# || is the SQLite concatenation operator.
sql = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X '

for i in cur.execute(sql):
	print (i)

cur.close()
