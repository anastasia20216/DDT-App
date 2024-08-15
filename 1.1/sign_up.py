import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from tkinter import ttk
# Function to create the database and the users table
def create_db():
    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Function to register a user
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    name = entry_name.get()

    if username == "" or password == "":
        messagebox.showerror("Input Error", "Please enter both username and password")
        return
    
    connection = sqlite3.connect('login.db')
    cursor = connection.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password, full_name) VALUES (?, ?, ?)', (username, password, name))
        connection.commit()
        messagebox.showinfo("Success", "Registration successful")
        subprocess.run(["python", "app2.0.py"])

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        connection.close()
        root.destroy()

# Create the main application window
root = tk.Tk()
root.geometry("400x450")
root.title("Registration Page")
root.configure(background='#FAF9F6')
bg=background='#FAF9F6'
style = ttk.Style(root)
style.theme_use('clam')
photo = tk.PhotoImage(file = "recipes.png")
photoimage = photo.subsample(1)
label_photo = tk.Label(root, image = photoimage,)
label_photo.pack(pady=25)
# Create and place the username label and entry
label_username = tk.Label(root, text="Username", background=bg)
label_username.pack(pady=10)
entry_username = tk.Entry(root, width=30)
entry_username.pack()

# Create and place the password label and entry
label_password = tk.Label(root, text="Password", background=bg)
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack()

label_name = tk.Label(root, text="Full Name", background=bg)
label_name.pack(pady=10)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

# Create and place the register button
button_register = ttk.Button(root, text="Sign up", command=register_user)
button_register.pack(pady=20)

# Call the function to create the database and table
create_db()

# Start the main event loop
root.mainloop()

