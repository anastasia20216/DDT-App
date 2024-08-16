from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

# Function to validate login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE users SET active_user = NULL")
    conn.commit()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    
    result = c.fetchone()
    
    
    if result:
        c.execute("UPDATE users SET active_user = 'yes' WHERE username=? AND password=?", (username, password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Login Success", "Welcome!")
        root.destroy()
        subprocess.run(["python", "app3.py"]) 
    else:
        conn.commit()
        conn.close()
        messagebox.showerror("Login Failed", "Invalid username or password")

def sign_up():
    root.destroy()
    subprocess.run(["python", "sign_up.py"])


# Initialize the main window
root = Tk()
root.title("Login Page")
root.geometry("400x450")
root.configure(background='#FAF9F6')
fr = Frame(root, )


#Title
label = Label(root, text='RECIPES', font=('Times', 30, 'bold'), bg='#FAF9F6')
label.grid(row=0, column=0, columnspan=2, padx=5, pady=40, sticky='nesw')

# Create and place the username label and entry
username_label = Label(root, text="Username:", background='#FAF9F6')
username_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
username_entry = Entry(root)
username_entry.grid(row=1, column=1, padx=5, pady=10, sticky='w')

# Create and place the password label and entry
password_label = Label(root, text="Password:", background='#FAF9F6')
password_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
password_entry = Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=15, sticky='w')

# Create and place the login button
login_button = Button(root, text="Login", command=validate_login, borderwidth=0.5, bg='#FAF9F6')
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the registration button
registration_button = Button(root, text="Sign up", command=sign_up, borderwidth=0.5, bg='#FAF9F6')
registration_button.grid(row=4, column=0, columnspan=2, pady=5)

# Adjust grid weights to center the content
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
