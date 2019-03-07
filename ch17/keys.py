import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

cur.execute('''CREATE TABLE PopByRegion ( Region TEXT NOT NULL, Population INTEGER NOT NULL, PRIMARY KEY (Region))''')
cur.execute('''CREATE TABLE PopByCountry(Region TEXT NOT NULL, Country TEXT NOT NULL, Population INTEGER NOT NULL, CONSTRAINT CountryKey PRIMARY KEY (Region, Country))''')

con.commit()
con.close()
