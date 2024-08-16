from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import subprocess
import tkinter as tk
import os
from tkinter import messagebox
#Establish main root window
root = Tk()
rep_name = ""
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
def profile():
    root.destroy()
    subprocess.run(["python", "user_pg.py"])
def login():
    root.destroy()
    subprocess.run(["python", "login.py"])     
 #This function gets called when a recipe button is clicked
def BtnClicked(rep_button, idx, rep_name):
    global selected_id
    selected_id = id_list[idx]
    print(idx)
    print(f"recipe id {selected_id} recipe name: {rep_name[idx]}")
    os.environ['id'] = str(selected_id)
    root.destroy()
    subprocess.run(["python", "recipe_pg.py"])
#Design root
root.title("Recipe")
root.geometry("1600x900")
root.config(bg='#F9F9F9')
# Database Connection and Data Retrieval
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
query_fav = "SELECT saved_rep FROM users WHERE active_user='yes'"
cursor.execute(query_fav)
row = cursor.fetchone()
#Checks if there are no recipes saved and displays 'no recipes saved' then gets saved data
if row == "":
    no_saved = Label(root, text="No recipes saved", bg='#FAF9F6', font=("Helvetica", 20, "bold"))
    no_saved.place(relx=0.3, rely=0.12)
if row:
    # row is a tuple so get the first element (the string)
    list_string = row[0].strip() if row[0] else ''
    if list_string == "":
        no_saved = Label(root, text="No recipes saved", bg='#FAF9F6', font=("Helvetica", 20, "bold"))
        no_saved.place(relx=0.18, rely=0.25)
    # Split the string into a list of strings
    str_values = list_string.split(', ')
        
        # Optionally, convert the list of strings to a list of integers
    id_list = [int(value) for value in str_values if value.isdigit()]
        
    print('Original Data:', list_string)
    print('Split List of Values:', str_values)
    print('List of Integers:', id_list)
else:
        # If the query returns None, get the user to log back in
    messagebox.showwarning(
        "Login Required",
        "You are not logged in. Please log in again."
        )
    login()

try:
    # Create placeholders for the SQL query
    placeholders = ', '.join(['?'] * len(id_list))

    # Create a CASE statement to order by the original list order
    order_by_case = ' '.join([f"WHEN ? THEN {i}" for i in range(len(id_list))])

    # SQL query that keeps the order of the original ID list
    query = f"""
    SELECT * FROM recipe
    WHERE id IN ({placeholders})
    ORDER BY CASE id {order_by_case} END
    """

    # Execute the query with the list of IDs twice (for WHERE and ORDER BY)
    cursor.execute(query, id_list + id_list)
    rows = cursor.fetchall()
    # Extract the names based on the column index
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

except sqlite3.Error as e:
    print(f"Database error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")





nav_bar = Frame(root, bg='#F5F2EB')
nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)

label = Label(nav_bar, text='RECIPES', font=('Times', 30, 'bold'), bg='#F5F2EB')
label.place(relx=0.8, rely=0.25)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.25)
Button(nav_bar, text='Search', relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.13, rely=0.25)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.23, rely=0.25)
Button(nav_bar, text="Profile", relief="flat", borderwidth=0, command=profile, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.33, rely=0.25)

Tilte = Label(root, text="Favorites", font=("Helvetica", 20, "bold"), bg='#FAF9F6')
Tilte.place(relx=0.15, rely=0.175)


x = 0.18 
y = 0.25
buttons = []

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