from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import subprocess
import tkinter as tk
root = Tk()
root.title("Title")
root.geometry("1600x900")
root.config(bg='#F9F9F9')
def show_recipes():
    root.destroy()
    subprocess.run(["python", "recipes.py"])
def show_fav():
    subprocess.run(["python", "favorite.py"])
    root.destroy()
def search():
    subprocess.run(["python", "search2.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app3.py"])
    root.destroy() 
def profile():
    subprocess.run(["python", "user_pg.py"])
    root.destroy() 
def rep_page():
    subprocess.run["python", "rep_page.py"]



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
        img = img.resize((225,150))  #Resize
        photo = ImageTk.PhotoImage(img)
        image_refs.append(photo)
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")
        # Handle error, maybe use a default image


side = Frame(root, bg='#F5F2EB')
side.place(relx=0, rely=0, relheight=1, relwidth=0.15)
nav_bar = Frame(root, bg='#F5F2EB')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='#F5F2EB')
label.place(relx=0.45, rely=0.2)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.2)
Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, command=show_recipes, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.1, rely=0.2)
Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.17, rely=0.2)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.24, rely=0.2)

logo = PhotoImage(file="profile.png").subsample(4)
Button(root, image=logo, bg='#F5F2EB', relief="flat", borderwidth=0, command=profile).place(relx=0.92, rely=0.01)

Font1 = ("Times", 14)
Label(side, text='CATEGORIES', font=Font1,  bg='#F5F2EB').place(relx=0.2, rely=0.15)

def print_button_value(value):
    global cat_value
    cat_value = value
    print(f"Button clicked with value: {value}")
    global buttons
    for button in buttons:
        button.destroy()
    buttons = []
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Use the selected ID from app3 to fetch the recipe details
    cat_id = (cat_value,) # Ensure it's a tuple with a single value
    query = "SELECT * FROM recipe WHERE cat=?"
    

    cursor.execute(query, cat_id)  # Execute the query with correct parameters
    rows = cursor.fetchall()  # Fetch the first matching row
    rep_name = [row[1] for row in rows]
    # Assuming the 5th column contains image paths
    rep_img_paths = [row[5] for row in rows]
    print(rep_img_paths)

    connection.close()

# Load Images using PIL and ImageTk
    rep_img_paths = [row[5] for row in rows]
    connection.close()

# Load Images using PIL and ImageTk
    image_refs = []
    for img_path in rep_img_paths:
        try:
            img = Image.open(img_path)
            img = img.resize((225,150))  #Resize
            photo = ImageTk.PhotoImage(img)
            image_refs.append(photo)
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
        # Handle error, maybe use a default image

    def BtnClicked(obj, idx, rep_name):
        global selected_id
        selected_id = idx + 1
        # This function gets called when a button is clicked
        print(f"recipe id {selected_id} recipe name: {rep_name[idx]}")
        subprocess.run(["python", "rep_page2.py"])
        root.destroy()
    x = 0.18 
    y = 0.15
    buttons = []
    for i in range(12):
        if i < len(rep_name):
            idx = i
            rep_button = Button(root, image=image_refs[i], text=rep_name[i], relief="flat", borderwidth=0, compound=TOP, bg='#F5F2EB', font=("Helvetica", 10), padx=5, pady=5)
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
           






k = 0.15
recipeframe = Frame(root, bg='#FAF9F6')
recipeframe.place(relx=0.15, rely=0.16, relheight=0.75, relwidth=0.84)

text1 = ['Vegetarian', 'Vegan', 'Chicken', 'Gluten Free', 'Healthy', 'Easy Meals', 'Lactose Free', 'Pasta']
k = 0.15
for category in text1:
    k += 0.05
    cat_button = Button(side, text=category, borderwidth=0.5, bg='#FAF9F6', font="Times 10",
                        command=lambda cat=category: print_button_value(cat))
    cat_button.place(relx=0.22, rely=k)
    




x = 0.18 
y = 0.15
buttons = []

def BtnClicked(obj, idx, rep_name):
    global selected_id
    selected_id = idx + 1
    # This function gets called when a button is clicked
    print(f"recipe id {selected_id} recipe name: {rep_name[idx]}")
    os.environ['id'] = str(selected_id)
    subprocess.run(["python", "rep_page2.py"])

    root.destroy()



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