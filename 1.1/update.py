import sqlite3

# connect to the database
conn = sqlite3.connect('data.db')

# create a cursor object
c = conn.cursor()

# update data in the table
c.execute("UPDATE recipe SET image = 'vegan-mushroom-cacciatore.png' WHERE id = '10'")

# save the changes
conn.commit()

conn.close()