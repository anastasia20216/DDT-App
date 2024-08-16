import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from tkinter import ttk
import re

#Function to validate the entered password
def validate_password(password):
    if len(password) < 5:
        return False, "Password must be at least 5 characters long."
    if not re.search(r'[a-zA-Z]', password):
        return False, "Password must contain at least one letter."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number."
    return True, ""



# Function to register a user
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    name = entry_name.get()
    active_user = 'yes'
    is_valid, message = validate_password(password)
    if is_valid:
        print("Success")
    else:
        messagebox.showerror("Error", message)
    if username == "" or password == "":
        messagebox.showerror("Input Error", "Please enter both username and password")
        return
    
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    try:
        cursor.execute("UPDATE users SET active_user = NULL")
        cursor.execute('INSERT INTO users (username, password, full_name, active_user) VALUES (?, ?, ?, ?)', (username, password, name, active_user))
        connection.commit()
        messagebox.showinfo("Success", "Registration successful")
        subprocess.run(["python", "app3.py"])

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        connection.close()
        root.destroy()

# Create the main application window
root = tk.Tk()
root.geometry("400x450")
root.title("Sign up Page")
root.configure(background='#FAF9F6')
bg=background='#FAF9F6'

#Title
label = tk.Label(root, text='RECIPES', font=('Times', 30, 'bold'), bg='#FAF9F6')
label.pack(pady=30)

# Create and place the name label and entry
label_name = tk.Label(root, text="Full Name", background=bg)
label_name.pack(pady=10)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

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

# Create and place the register button
button_register = tk.Button(root, text="Sign up", command=register_user, borderwidth=0.5, bg='#FAF9F6')
button_register.pack(pady=20)



# Start the main event loop
root.mainloop()

