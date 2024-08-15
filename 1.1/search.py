import tkinter as tk
from tkinter import ttk
import subprocess
# Function to handle the search button click event
def perform_search():
    query = entry.get()
    print(f"Search query: {query}")

def show_recipes():
    root.destroy()
    subprocess.run(["python", "recipes.py"])
def exit_app():
    root.destroy()
def show_categories():
    pass  # Add your category display logic here
def show_fav():
    root.destroy()
def search():
    root.destroy()
    subprocess.run(["python", "search2.0.py"])
def home():
    root.destroy()
    subprocess.run(["python", "app2.0.py"])

# Initialize the main window
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='#FAF9F6')
root.title("Search Page")
style = ttk.Style(root)
style.theme_use('clam')
style.configure('Button', background='white')
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
side = tk.Frame(root, bg='#efeee8')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)
nav_bar = tk.Frame(root, bg='#efeee8')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = tk.Label(nav_bar, text='Recipes', font="Times 26 bold")
label.place(relx=0.45, rely=0.2)

ttk.Button(nav_bar, text='Home', command=home, padding=(6, 8)).place(relx=0.03, rely=0.2)
ttk.Button(nav_bar, text='Recipes', command=show_recipes, padding=(6, 8)).place(relx=0.1, rely=0.2)
ttk.Button(nav_bar, text="Exit", command=exit_app, padding=(6,8)).place(relx=0.17, rely=0.2)
ttk.Button(nav_bar, text="Favorites", command=show_fav, padding=(6,8)).place(relx=0.24, rely=0.2)
ttk.Button(nav_bar, text="Search", command=search, padding=(6,8)).place(relx=0.32, rely=0.2)

# Create a frame for centering the search bar
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create and place the search bar (Entry widget)
entry = tk.Entry(frame, width=50, font=('Arial', 14), background='#FAF9F6')
entry.grid(row=0, column=0, padx=10, pady=20)

# Create and place the search button
search_button = tk.Button(frame, text="Search", font=('Arial', 14), command=perform_search)
search_button.grid(row=0, column=1)

# Start the Tkinter event loop
root.mainloop()