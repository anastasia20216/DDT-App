import tkinter as tk
from tkinter import messagebox
import sqlite3

def search_database():
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
    if results:
        for row in results:
            result_text.insert(tk.END, row[1] + '\n')
    else:
        result_text.insert(tk.END, "No results found.")




root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='#FAF9F6')
root.title("Search Page")
side = tk.Frame(root, bg='#efeee8')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)
nav_bar = tk.Frame(root, bg='#efeee8')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = tk.Label(nav_bar, text='Recipes', font="Times 26 bold")
label.place(relx=0.45, rely=0.2)
import subprocess

def show_recipes():
    root.destroy()
    subprocess.run(["python", "recipes.py"])
def show_categories():
    pass  # Add your category display logic here
def show_fav():
    subprocess.run(["python", "favorites.py"])
    root.destroy()
def search():
    subprocess.run(["python", "search.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app2.0.py"])
    root.destroy() 
tk.Button(nav_bar, text='Home', command=home).place(relx=0.03, rely=0.2)
tk.Button(nav_bar, text='Recipes', command=show_recipes).place(relx=0.1, rely=0.2)
tk.Button(nav_bar, text="Favorites", command=show_fav).place(relx=0.24, rely=0.2)
tk.Button(nav_bar, text="Search", command=search).place(relx=0.32, rely=0.2)



# Create and place the search bar (Entry widget)
entry = tk.Entry(root, width=50, font=('Arial', 14), background='#FAF9F6')
entry.place(relx=0.3, rely=0.15)

# Create and place the search button
search_button = tk.Button(root, text="Search", font=('Arial', 14), command=search_database)
search_button.place(relx=0.7, rely=0.14)
result_text = tk.Text(root, width=100, height=30)
result_text.place(relx=0.3, rely=0.2) 
# Start the Tkinter event loop
root.mainloop()