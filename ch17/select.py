#!/usr/bin/env python3

import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

cur.execute('SELECT Region, Population FROM PopByRegion')
#print(cur.fetchone())
print(cur.fetchall())
cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
print(cur.fetchall())
cur.execute('''SELECT Region, Population FROM PopByRegion ORDER BY Population DESC''')
print(cur.fetchall())
cur.execute('SELECT Region FROM PopByRegion')
print(cur.fetchall())
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())
cur.execute('SELECT Region FROM PopByRegion WHERE Population > 500000')
print(cur.fetchall())
cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"''')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchall())
cur.execute('DELETE FROM PopByRegion WHERE Region < "G"')
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

con.commit()




