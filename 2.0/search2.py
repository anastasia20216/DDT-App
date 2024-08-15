from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
import os
import sys



def search_database():
    global keyword
    keyword = entry.get()
    print("searching " + keyword)
    os.environ['keyword'] = str(keyword)

    if not keyword:
        messagebox.showwarning("Input Error", "Please enter a keyword to search.")
        return

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM recipe WHERE
    recipe_name LIKE ? OR
    method LIKE ? OR
    ingridents LIKE ?
    """
    params = ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%')
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    
    display_results(results)


no_recipe = None
global buttons
buttons = []
def display_results(results):
    global buttons
    repeat=0.1
    all_results = []
    global no_recipe
    if buttons:
        for button in buttons:
    # Check if the button is not None
            button.destroy()
    buttons = []
    # Check if no_recipe exists before destroying it
    if no_recipe is not None:
        no_recipe.destroy()
        no_recipe = None  # Reset no_recipe after destruction
    

    if results:
        for row in results:
            repeat += 0.07
            recipe_id = row[0]
            recipe_name = row[1]
            method = row[3]
            ingredients = row[4]
            ima = row[5]
            

            # Append each result to the global list as a dictionary
            all_results.append({
                "id": recipe_id,
                "name": recipe_name,
                "method": method,
                "ingredients": ingredients,
                "image": ima
            })
            
           

        # Handle error, maybe use a default image

            rep_button = Button(results_frame, text=f"{recipe_name}", relief="flat", compound=TOP, borderwidth=1, height=1, bg='#F5F2EB', padx=3, pady=3)
            rep_button.place(relx=0.1, rely=repeat)

            rep_button.config(command=lambda b=rep_button, id=recipe_id, v=recipe_name: BtnClicked(b, id, v))
            buttons.append(rep_button)
    else:
        no_recipe = Label(root, text="No recipe found for:  " + keyword, font=("Helvetica", 12), bg='#FAF9F6')
        no_recipe.place(relx=0.3, rely=0.2)
        
        
            
def BtnClicked(obj, recipe_id, recipe_name):
    global selected_id
    selected_id = recipe_id 
    # This function gets called when a button is clicked
    print(f"recipe id {selected_id} recipe name: {recipe_name[recipe_id]}")
    # Example of a unique action
    os.environ['ids'] = str(selected_id)
    subprocess.run(["python", "searchrep.py"])
    root.destroy()




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
     


root = Tk()
root.title("Search")
root.geometry("1600x900")
root.config(bg='#FAF9F6')

nav_bar = Frame(root, bg='#F5F2EB')
nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)

results_frame = Frame(root, bg='#FAF9F6')
results_frame.place(relx=0.25, rely=0.14, relheight=0.6, relwidth=0.6)

label = Label(nav_bar, text='RECIPES', font=('Times', 30, 'bold'), bg='#F5F2EB')
label.place(relx=0.8, rely=0.25)

Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.25)
Button(nav_bar, text='Search', relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.13, rely=0.25)
Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.23, rely=0.25)
Button(nav_bar, text="Profile", relief="flat", borderwidth=0, command=profile, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.33, rely=0.25)


# Create and place the search bar (Entry widget)
entry = Entry(root, width=50, font=('Arial', 14), background='#FAF9F6')
entry.focus_set()
entry.bind("<Return>", lambda e: search_database())
entry.place(relx=0.3, rely=0.15)
if len(sys.argv) > 1:
    key = sys.argv[1]
    print(f"Received key: {key}")
    entry.insert(0,str(key))
    search_database()
# Create and place the search button
search_button = Button(root, text="Search", font=('Arial', 14), command=search_database)

search_button.place(relx=0.7, rely=0.14)

# Start the Tkinter event loop


result_button = Button(root, relief="flat", borderwidth=0, compound=TOP, bg='#FAF9F6').place(relx=0.2, rely=0.19)


root.mainloop()