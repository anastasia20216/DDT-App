from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import subprocess
root = Tk()
root.title("Title")
root.geometry("1600x900")
root.config(bg='#FAF9F6')
def show_recipes():
    root.destroy()
    subprocess.run(["python", "recipes.py"])
def show_categories():
    pass  # Add your category display logic here
def show_fav():
    subprocess.run(["python", "favorite.py"])
    root.destroy()
def search():
    subprocess.run(["python", "search2.0.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app1.1.py"])
    root.destroy() 
def profile():
    subprocess.run(["python", "user_pg.py"])
    root.destroy() 


# Database Connection and Data Retrieval
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query = "SELECT * FROM recipe"
cursor.execute(query)
rows = cursor.fetchall()
column_index = 1 
rep_name = [row[column_index] for row in rows]

# Assuming the 5th column contains image paths
rep_img_paths = [row[5] for row in rows]
connection.close()

# Load Images using PIL and ImageTk
image_refs = []
for img_path in rep_img_paths:
    try:
        img = Image.open(img_path)
        img = img.resize((200,133))  #Resize
        photo = ImageTk.PhotoImage(img)
        image_refs.append(photo)
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")
        # Handle error, maybe use a default image



nav_bar = Frame(root, bg='#FAF9F6')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='#FAF9F6')
label.place(relx=0.45, rely=0.2)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.2)
Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, command=show_recipes, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.1, rely=0.2)
Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.17, rely=0.2)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.24, rely=0.2)

logo = PhotoImage(file="profile.png").subsample(4)
Button(root, image=logo, bg='#FAF9F6', relief="flat", borderwidth=0, command=profile).place(relx=0.92, rely=0.01)


root.mainloop()