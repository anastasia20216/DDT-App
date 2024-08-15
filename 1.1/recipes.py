from tkinter import *
root = Tk()
root.geometry("1600x900")
import subprocess
from PIL import Image, ImageTk
def show_recipes():
    root.destroy()
    subprocess.run(["python", "recipes.py"])
def exit_app():
    root.destroy()
def show_categories():
    pass  # Add your category display logic here
def show_fav(): 
    root.destroy()
def search():
    subprocess.run(["python", "search.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app2.0.py"])
    root.destroy() 

import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query = "SELECT * FROM recipe"
cursor.execute(query)
rows = cursor.fetchall()
column_index = 1 
# Correct way to use list comprehension to extract a specific column from each row
rep_name = [row[column_index] for row in rows]

rep_img = [row[5] for row in rows]
connection.close()


root.config(bg="white")
side = Frame(root, bg='light grey')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)
nav_bar = Frame(root, bg='light grey')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='light grey')
label.place(relx=0.45, rely=0.2)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home).place(relx=0.03, rely=0.2, relheight=0.4, relwidth=0.04)
Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, command=show_recipes).place(relx=0.1, rely=0.2)
Button(nav_bar, text="Exit", relief="flat", borderwidth=0, command=exit_app).place(relx=0.17, rely=0.2)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav).place(relx=0.24, rely=0.2)
Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search).place(relx=0.32, rely=0.2)


logo = PhotoImage(file="logo.png").zoom(3).subsample(6)
Label(root, image=logo).place(relx=0.9, rely=0.006)

Label(root, text="Search", bg="light grey").place(relx=0.03, rely=0.08)
search_bar = Entry(root)
search_bar.place(relx=0.03, rely=0.1, relheight=0.03, relwidth=0.14)

Font1 = ("Times", 16)
Label(root, text='CATEGORIES', font=Font1,  bg='light grey').place(relx=0.03, rely=0.15)

Label(root, text='HEADING', font=Font1, bg='white').place(relx=0.22, rely=0.15)
photo = PhotoImage(file="download.png").zoom(25).subsample(32)
for i in range(5):
    print(rep_img[i])
for i in range(5):
    Button(root, image=rep_img[i], text=rep_name[i], relief="flat", borderwidth=0, compound=TOP).place(relx=0.2 + 0.16*i, rely=0.19)
for i in range(5):
    Button(root, image=rep_img[i], text=rep_name[i], relief="flat", borderwidth=0, compound=TOP).place(relx=0.2 + 0.16*i, rely=0.45)
for i in range(5):
    Button(root, image=rep_img[i], text=rep_name[i], relief="flat", borderwidth=0, compound=TOP).place(relx=0.2 + 0.16*i, rely=0.7)


root.mainloop()