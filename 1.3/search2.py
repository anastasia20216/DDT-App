import subprocess
import sqlite3
from tkinter import *
from tkinter import messagebox

def search_database():
    """
    Search the database for recipes matching the keyword entered in the entry widget.
    """
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
    ingredients LIKE ?
    """
    params = ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%')
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    
    display_results(results)

def display_results(results):
    """
    Display the search results in the results frame.
    """
    global buttons
    buttons = []

    # Clear previous results
    for button in buttons:
        if button:
            button.pack_forget()

    if results:
        repeat = 0.2
        all_results = []

        for row in results:
            repeat += 0.05
            recipe_id, recipe_name, method, ingredients, image = row

            all_results.append({
                "id": recipe_id,
                "name": recipe_name,
                "method": method,
                "ingredients": ingredients,
                "image": image
            })

            # Create and place a button for each result
            rep_button = Button(
                results_frame, text=recipe_name, compound=TOP, relief="flat", borderwidth=2, height=1
            )
            rep_button.place(relx=0.25, rely=repeat)
            rep_button.config(command=lambda b=rep_button, id=recipe_id, name=recipe_name: btn_clicked(b, id, name))
            buttons.append(rep_button)
    else:
        no_recipe = Label(
            root, text=f"No recipe found for: {entry.get()}", font=("Helvetica", 12), bg='#FAF9F6'
        )
        no_recipe.place(relx=0.3, rely=0.2)

def btn_clicked(button, recipe_id, recipe_name):
    """
    Handle button click event to show the selected recipe.
    """
    global selected_id
    selected_id = recipe_id
    # Example of a unique action
    print(f"Recipe ID: {selected_id}, Recipe Name: {recipe_name}")
    subprocess.run(["python", "app.py"])
    root.destroy()

def show_recipes():
    """
    Open the recipes window.
    """
    root.destroy()
    subprocess.run(["python", "recipes.py"])

def show_favorites():
    """
    Open the favorites window.
    """
    subprocess.run(["python", "favorites.py"])
    root.destroy()

def search():
    """
    Open the search window.
    """
    subprocess.run(["python", "search2.0.py"])
    root.destroy()

def home():
    """
    Open the home window.
    """
    subprocess.run(["python", "app1.1.py"])
    root.destroy()

def profile():
    """
    Open the user profile window.
    """
    subprocess.run(["python", "user_pg.py"])
    root.destroy()

# Initialize the main Tkinter window
root = Tk()
root.title("Title")
root.geometry("1600x900")
root.config(bg='#FAF9F6')

# Create and place side and nav_bar frames
side = Frame(root, bg='#FAF9F6')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)

nav_bar = Frame(root, bg='#FAF9F6')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

# Create and place labels and buttons in nav_bar
Label(
    nav_bar, text='Recipes', font="Times 30 bold", bg='#FAF9F6'
).place(relx=0.45, rely=0.2)

Button(
    nav_bar, text='Home', relief="flat", borderwidth=0, command=home,
    width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12"
).place(relx=0.03, rely=0.2)

Button(
    nav_bar, text='Recipes', relief="flat", borderwidth=0, command=show_recipes,
    width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12"
).place(relx=0.1, rely=0.2)

Button(
    nav_bar, text="Search", relief="flat", borderwidth=0, command=search,
    width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12"
).place(relx=0.17, rely=0.2)

Button(
    nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_favorites,
    width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12"
).place(relx=0.24, rely=0.2)

# Create and place the profile button
logo = PhotoImage(file="profile.png").subsample(4)
Button(
    root, image=logo, bg='#FAF9F6', relief="flat", borderwidth=0, command=profile
).place(relx=0.92, rely=0.01)

# Create and place the search bar and search button
entry = Entry(root, width=50, font=('Arial', 14), background='#FAF9F6')
entry.place(relx=0.3, rely=0.15)

search_button = Button(
    root, text="Search", font=('Arial', 14), command=search_database
)
search_button.place(relx=0.7, rely=0.14)

# Create and place the results frame
results_frame = Frame(root, bg='#FAF9F6')
results_frame.place(relx=0.3, rely=0.3, relheight=0.8, relwidth=0.6)

# Start the Tkinter event loop
root.mainloop()
