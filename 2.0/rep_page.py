from tkinter import *
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk
import app3
print(app3.idx)
print(app3.selected_id)


def search():
    subprocess.run(["python", "search2.0.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app3.py"])
    root.destroy() 

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
rep_id = (app3.selected_id,)
query = "SELECT id, recipe_name, ingridents, method, image FROM recipe WHERE id=?",(rep_id)
cursor.execute(query)
row = cursor.fetchone()
#method = row[3].split('Step')
method = re.split(r'(?=Step)', row[3])

root = Tk()
root.title("Title")
root.geometry("1600x900")
root.config(bg='#FAF9F6')
nav_bar = Frame(root, bg='#FAF9F6')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='#FAF9F6')
label.place(relx=0.45, rely=0.2)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.2)
Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.1, rely=0.2)
Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.17, rely=0.2)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.24, rely=0.2)

logo = PhotoImage(file="profile.png").subsample(4)
Label(root, image=logo, bg='#FAF9F6').place(relx=0.92, rely=0.01)

root.mainloop()