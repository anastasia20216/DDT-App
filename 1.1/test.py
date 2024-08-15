import sqlite3

# Connect to the SQLite database 
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query to select all data from a specific table 
query = "SELECT * FROM recipe"

# Execute the query
cursor.execute(query)

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Loop through each row and display the data from a specific column (replace 'column_index' with the column index)
column_index = 1  # Assuming you want to display the second column (index starts at 0)
for row in rows:
    print(row[column_index])

# Close the connection
connection.close()
