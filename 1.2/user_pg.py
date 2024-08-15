from tkinter import *
import subprocess
import sqlite3

def show_recipes():
    subprocess.run(["python", "recipes.py"])
    root.destroy()
def show_fav():
    root.destroy()
    subprocess.run(["python", "fav_reps.py"])
def search():
    root.destroy()
    subprocess.run(["python", "search2.py"])
def home():
    root.destroy()
    subprocess.run(["python", "app3.py"])
def signout():
    root.destroy()
    subprocess.run(["python", "login.py"])
    


connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query = cursor.execute("SELECT * FROM users WHERE active_user='yes'")
row = cursor.fetchone()



root = Tk()
root.title("Title")
root.geometry("1600x900")
root.config(bg='#FAF9F6')
nav_bar = Frame(root, bg='#FAF9F6')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='#FAF9F6')
label.place(relx=0.45, rely=0.2)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.2)
Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, command=show_recipes, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.1, rely=0.2)
Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.17, rely=0.2)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.24, rely=0.2)

logo = PhotoImage(file="profile.png").subsample(4)
Label(root, image=logo, bg='#FAF9F6').place(relx=0.92, rely=0.01)

user_info = Label(root, text='Profile', font='times, 18', bg='#FAF9F6').place(relx=0.3, rely=0.2, relheight=0.05, relwidth=0.4)
full_name = Label(root, text='Full Name: ' + row[3], font='times, 14', bg='#FAF9F6').place(relx=0.4, rely=0.35)
username = Label(root, text='Username: ' + row[1], font='times, 14', bg='#FAF9F6').place(relx=0.4, rely=0.4)
password = Label(root, text='Password: ' + row[2], font='times, 14', bg='#FAF9F6').place(relx=0.4, rely=0.45)
sign_out = Button(root, text='sign out', command=signout, font='times, 14', bg='#F9F9F9').place(relx=0.48, rely=0.55)
root.mainloop()