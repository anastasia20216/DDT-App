from tkinter import *
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk
def show_recipes():
    root.destroy()
    subprocess.run(["python", "app1.1.py"])
def show_categories():
    pass  # Add your category display logic here
def show_fav():
    subprocess.run(["python", "favorites.py"])
    root.destroy()
def search():
    subprocess.run(["python", "search2.0.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app1.1.py"])
    root.destroy() 

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query = "SELECT id, recipe_name, ingridents, method, image FROM recipe WHERE id=1"
cursor.execute(query)
row = cursor.fetchone()
#method = row[3].split('Step')
method = re.split(r'(?=Step)|(?=butter)', row[3])

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

method_frame = Frame(root, bg='#FAF9F6').place(relx=0.25, rely=0.15, relheight=0.7, relwidth=0.6)
title = Label(root, text=row[1], font='times, 18').place(relx=0.1, rely=0.1, relheight=0.08, relwidth=0.4)
repeat = 0
for i in range(len(method)):
    repeat += 0.05
    Label(root, text=method[i], font='times, 12', bg='#FAF9F6').place(relx=0.3, rely=0.15+repeat)


ingridents = Label(root, text=row[2], font='times, 12', bg='#FAF9F6').place(relx=0.03, rely=0.25, relheight=0.35, relwidth=0.23)
#method = Label(root, text=row[3], font='times, 14', anchor='w').place(relx=0.3, rely=0.2, relheight=0.7, relwidth=0.8)
img = Image.open(row[4])
img = img.resize((300,200))  #Resize
photo = ImageTk.PhotoImage(img)
ima = Label(root, image=photo).place(relx=0.75, rely=0.15)

root.mainloop()