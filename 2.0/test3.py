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
#This function gets called when a catorgory button is clicked and saves 
# the id value that is then used in the next page
def print_button_value(value):
    print(f"Button clicked with value: {value}")
    global buttons
    for button in buttons:
        button.destroy()
    buttons = []
    os.environ['cat_id'] = value
    subprocess.run(["python", "rep_cat.py"])
    root.destroy() 
 #This function gets called when a recipe button is clicked
def BtnClicked(rep_button, idx, rep_name):
    selected_id = idx + 1
    print(f"recipe id {selected_id} recipe name: {rep_name[idx]}")
    os.environ['id'] = str(selected_id)
    root.destroy()
    subprocess.run(["python", "rep_fav_feature_test.py"])

root = tk.Tk()
root.title("Recipes")
root.geometry("1600x900")
# Create a Canvas widget
canvas = tk.Canvas(root, bg='#FAF9F6')
canvas.pack(side='left', fill='both', expand=True)
root.config(bg='#F9F9F9')
# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
# Configure the Canvas to work with the scrollbar
canvas.config(yscrollcommand=scrollbar.set)
# Create a Frame to hold the buttons
button_frame = tk.Frame(canvas, bg='#FAF9F6')
canvas.create_window((0, 0), window=button_frame, anchor='nw')
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
        base ='C:/Users/anast/OneDrive/Documents/computer science/L3 Python/Development Log/2.0/images'
        full_path = os.path.join(base, img_path)
        img = Image.open(full_path)
        img = img.resize((225,150))  #Resize
        photo = ImageTk.PhotoImage(img)
        image_refs.append(photo)
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")
        # Handle error

#Frames of the top bar
#nav_bar = Frame(root, bg='#F5F2EB')
#nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)
hungry = PhotoImage(file="hungry.png")

#Title
#label = Label(nav_bar, text='RECIPES', font=('Times', 30, 'bold'), bg='#F5F2EB')
#label.place(relx=0.8, rely=0.25)

#Nav_bar Buttons
#Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.25)
#Button(nav_bar, text='Search', relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.13, rely=0.25)
#Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.23, rely=0.25)
#Button(nav_bar, text="Profile", relief="flat", borderwidth=0, command=profile, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.33, rely=0.25)

#ponistioning for recipe bttons
x = 0.18 
y = 0.15
buttons = []
#Main page recipes, button images with data from the recipe database
for i in range(12):
    if i < len(rep_name):
        idx = i
        rep_button = tk.Button(button_frame, image=image_refs[i], text=rep_name[i], relief="flat", borderwidth=0, compound=TOP, bg='#F5F2EB', font=("Helvetica", 10), padx=5, pady=5)
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
# Update the Canvas scroll region to encompass the button_frame
button_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))
root.mainloop()