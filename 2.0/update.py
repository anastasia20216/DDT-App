import sqlite3

# connect to the database
conn = sqlite3.connect('data.db')

# create a cursor object
c = conn.cursor()
#text1 = ['vegetarian', 'Vegen', 'chicken', 'gluten free', 'healthy', 'easy meals', 'lactose free', 'pasta']
# update data in the table
c.execute("UPDATE recipe SET cat = 'vegan' WHERE id in ()")
#new_column = "ALTER TABLE recipe ADD COLUMN cat TEXT"
#c.execute(new_column)
# save the changes
conn.commit()

conn.close()