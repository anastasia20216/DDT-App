from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
import os


def search_database():
    global keyword
    keyword = entry.get()

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

def display_results(results):
        

    repeat=0.15
    all_results = []
    global buttons
   
    for button in buttons:
        button.destroy()
    buttons = []

    if results:
        for row in results:
            repeat += 0.05
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
            rep_button.place(relx=0.25, rely=repeat)
            Label(results_frame, text=" ", bg='#FAF9F6')
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
root.title("Title")
root.geometry("1600x900")
root.config(bg='#FAF9F6')
side = Frame(root, bg='#FAF9F6')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)
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


# Create and place the search bar (Entry widget)
entry = Entry(root, width=50, font=('Arial', 14), background='#FAF9F6')
entry.place(relx=0.3, rely=0.15)

# Create and place the search button
search_button = Button(root, text="Search", font=('Arial', 14), command=search_database)
search_button.place(relx=0.7, rely=0.14)

# Start the Tkinter event loop
global buttons
buttons = []

result_button = Button(root, relief="flat", borderwidth=0, compound=TOP, bg='#FAF9F6').place(relx=0.2, rely=0.19)
results_frame = Frame(root, bg='#FAF9F6').place(relx=0.3, rely=0.3, relheight=0.8, relwidth=0.6)

root.mainloop()