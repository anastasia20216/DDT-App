from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import subprocess
import tkinter as tk
import os
def show_fav():
    root.destroy()
    subprocess.run(["python", "fav_reps.py"])
def search():
    root.destroy()
    subprocess.run(["python", "search2.py"])
def home():
    root.destroy()
    subprocess.run(["python", "app3.py"])
def profile():
    root.destroy()
    subprocess.run(["python", "user_pg.py"])
def login():
    root.destroy()
    subprocess.run(["python", "login.py"])
    update_button()

#This function checks if user is logged in
def is_logged_in():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM users WHERE active_user='yes'")
    row = cursor.fetchone()
    connection.close()
    return row is not None

#Changes login button to profile button
def update_button():
    if is_logged_in():
        login_btn.config(text="Profile", command=profile)
    else:
        login_btn.config(text="Login", command=login)


#This function gets called when a catorgory button is clicked and saves 
# the id value that is then used in the next page
def print_button_value(value):
    print(f"Button clicked with value: {value}")
    global buttons
    for button in buttons:
        button.destroy()
    buttons = []
    os.environ['cat_id'] = value
    root.destroy() 
    subprocess.run(["python", "rep_cat.py"])

 #This function gets called when a recipe button is clicked
def BtnClicked(rep_button, idx, rep_name):
    selected_id = idx + 1
    print(f"recipe id {selected_id} recipe name: {rep_name[idx]}")
    os.environ['id'] = str(selected_id)
    root.destroy()
    subprocess.run(["python", "recipe_pg.py"])

#Establish main root window
root = Tk()
root.title("Recipes")
root.geometry("1600x900")
root.config(bg='#F9F9F9')
# Database Connection and Data Retrieval
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query = "SELECT * FROM recipe"
cursor.execute(query)
rows = cursor.fetchall()
column_index = 1 
rep_name = [row[column_index] for row in rows]
rep_img_paths = [row[5] for row in rows]
connection.close()

# Load Images using PIL and ImageTk
image_refs = []
for img_path in rep_img_paths:
    try:
        path = img_path
        base ='images'
        full_path = os.path.join(base, img_path)
        img = Image.open(full_path)
        img = img.resize((225,150))  #Resize
        photo = ImageTk.PhotoImage(img)
        image_refs.append(photo)
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")
        # Handle error

#Frames of the top bar and side bar
side = Frame(root, bg='#FAF9F6')
side.place(relx=0, rely=0, relheight=1, relwidth=0.15)
nav_bar = Frame(root, bg='#F5F2EB')
nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)


#Title
label = Label(nav_bar, text='RECIPES', font=('Times', 30, 'bold'), bg='#F5F2EB')
label.place(relx=0.8, rely=0.25)

#Nav_bar Buttons
Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.25)
Button(nav_bar, text='Search', relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.13, rely=0.25)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.23, rely=0.25)
login_btn = Button(nav_bar, text="", relief="flat", borderwidth=0, command=None, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12")
login_btn.place(relx=0.33, rely=0.25)
update_button()
#Categories and category buttons
Font1 = ("Times", 14)
Label(side, text='CATEGORIES', font=Font1,  bg='#F9F9F9').place(relx=0.2, rely=0.15)
k = 0.15
recipeframe = Frame(root, bg='#FAF9F6')
recipeframe.place(relx=0.15, rely=0.16, relheight=0.75, relwidth=0.84)
text1 = ['Vegetarian', 'Vegan', 'Chicken', 'Gluten Free', 'Healthy', 'Easy Meals', 'Lactose Free', 'Pasta']
k = 0.15
for category in text1:
    k += 0.05
    cat_button = Button(side, text=category, borderwidth=0.5, bg='#FAF9F6', font=("Helvetica", 10),command=lambda cat=category: print_button_value(cat))
    cat_button.place(relx=0.22, rely=k)

#Ponistioning for recipe bttons
x = 0.18 
y = 0.15
buttons = []
#Main page recipes, button images with data from the recipe database
for i in range(12):
    if i < len(rep_name):
        idx = i
        rep_button = tk.Button(root, image=image_refs[i], text=rep_name[i], relief="flat", borderwidth=0, compound=TOP, bg='#F5F2EB', font=("Helvetica", 10), padx=5, pady=5)
        rep_button.place(relx=x, rely=y)
        x += 0.2
        rep_button.config(command=lambda b=rep_button, id=idx, v=rep_name: BtnClicked(b, id, v))
        buttons.append(rep_button)
        if i == 3:
            y += 0.25
            x = 0.18
        if i == 7:
            y += 0.25
            x = 0.18

root.mainloop()