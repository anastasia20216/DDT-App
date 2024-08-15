import subprocess
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
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
    subprocess.run(["python", "search2.0.py"])
    root.destroy()
def home():
    subprocess.run(["python", "app2.0.py"])
    root.destroy() 

root = tk.Tk()
root.title("Title")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='#FAF9F6')
style = ttk.Style(root)
style.theme_use('clam')
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
side = tk.Frame(root, bg='#efeee8')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)
nav_bar = tk.Frame(root, bg='#efeee8')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = tk.Label(nav_bar, text='Recipes', font="Times 26 bold")
label.place(relx=0.45, rely=0.2)

ttk.Button(nav_bar, text='Home', command=home, padding=(6, 8), style='Custom.TButton').place(relx=0.03, rely=0.2)
ttk.Button(nav_bar, text='Recipes', command=show_recipes, padding=(6, 8)).place(relx=0.1, rely=0.2)
ttk.Button(nav_bar, text="Exit", command=exit_app, padding=(6,8)).place(relx=0.17, rely=0.2)
ttk.Button(nav_bar, text="Favorites", command=show_fav, padding=(6,8)).place(relx=0.24, rely=0.2)
ttk.Button(nav_bar, text="Search", command=search, padding=(6,8)).place(relx=0.32, rely=0.2)


thecookbook = tk.PhotoImage(file="thecookbook.png").zoom(3).subsample(5)
tk.Label(root, image=thecookbook).place(relx=0.7, rely=0.1)
logo = tk.PhotoImage(file="logo.png").zoom(3).subsample(5)
tk.Label(root, image=logo).place(relx=0.9, rely=0)


search_bar = tk.Entry(root)
search_bar.place(relx=0.03, rely=0.1, relheight=0.03, relwidth=0.14)

Font1 = ("Times", 14, "bold")
tk.Label(root, text='CATEGORIES', font=Font1).place(relx=0.03, rely=0.15)

# Load image once and reuse for buttons
text1 = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item6', 'item6']
for i in range(8):
    ttk.Button(root, text=text1[i], padding=(2,8), ).place(relx=0.04, rely=0.2 + 0.06*i)


tk.Label(root, text='HEADING', font=Font1).place(relx=0.22, rely=0.15)
photo = tk.PhotoImage(file="download.png").zoom(25).subsample(32)
for i in range(5):
    tk.Button(root, image=photo, relief='flat', borderwidth=0).place(relx=0.2 + 0.16*i, rely=0.6)

for i in range(5):
    tk.Button(root, image=photo, relief='flat', borderwidth=0).place(relx=0.2 + 0.16*i, rely=0.3)

root.mainloop()