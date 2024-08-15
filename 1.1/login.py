import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from tkinter import ttk
# Function to validate login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    
    if result:
        messagebox.showinfo("Login Success", "Welcome!")
        root.destroy()
        subprocess.run(["python", "app2.0.py"]) 
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def sign_up():
    root.destroy()
    subprocess.run(["python", "sign_up.py"])


# Initialize the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x450")
root.configure(background='#FAF9F6')
fr = tk.Frame(root, )
style = ttk.Style(root)
style.theme_use('clam')
# Create a photoimage object of the image in the path
photo = tk.PhotoImage(file="recipes.png")

# Create and place the image
image_label = tk.Label(root, image=photo, background='#FAF9F6')
image_label.grid(row=0, column=0, columnspan=2, pady=(40, 20))

# Create and place the username label and entry
username_label = tk.Label(root, text="Username:", background='#FAF9F6')
username_label.grid(row=1, column=0, padx=20, pady=10, sticky='e')
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=5, pady=10, sticky='w')

# Create and place the password label and entry
password_label = tk.Label(root, text="Password:", background='#FAF9F6')
password_label.grid(row=2, column=0, padx=20, pady=10, sticky='e')
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=15, sticky='w')

# Create and place the login button
login_button = ttk.Button(root, text="Login", command=validate_login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the registration button
registration_button = ttk.Button(root, text="Sign up", command=sign_up)
registration_button.grid(row=4, column=0, columnspan=2, pady=5)

# Adjust grid weights to center the content
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
