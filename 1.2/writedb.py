import sqlite3

def check_database_connection(data, recipe):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        print(f"Successfully connected to the database '{data}'.")

        # Check if the table exists
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{recipe}';")
        table_exists = cursor.fetchone()

        if table_exists:
            print(f"Table '{recipe}' exists in the database.")
            
            # Retrieve some data from the table to check if changes were committed
            cursor.execute(f"SELECT * FROM {recipe} LIMIT 5;")
            rows = cursor.fetchall()

            if rows:
                print("Previous changes have been committed. Here are some records:")
                for row in rows:
                    print(row)
            else:
                print("The table is empty or no changes have been committed yet.")
        else:
            print(f"Table '{recipe}' does not exist in the database.")
        
        # Close the connection
        cursor.close()
        connection.close()
        print("Database connection closed.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Replace 'your_database.db' and 'your_recipe' with your database and table names
check_database_connection('data', 'recipe')