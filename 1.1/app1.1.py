from tkinter import *
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
Label(root, image=logo, bg='#FAF9F6').place(relx=0.92, rely=0.01)

Label(root, text="Search", bg="#FAF9F6", font="Times, 13").place(relx=0.03, rely=0.09)
search_bar = Entry(root)
search_bar.place(relx=0.03, rely=0.12, relheight=0.03, relwidth=0.14)

Font1 = ("Times", 14)
Label(root, text='CATEGORIES', font=Font1,  bg='#FAF9F6').place(relx=0.03, rely=0.15)

# Load image once and reuse for buttons
text1 = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item6', 'item6']
for i in range(8):
    Button(root, text=text1[i], relief="flat", borderwidth=0, bg='#FAF9F6', font="Times, 10").place(relx=0.04, rely=0.2 + 0.06*i)



photo = PhotoImage(file="download.png").zoom(25).subsample(32)
for i in range(5):
    Button(root, image=photo, relief="flat", borderwidth=0).place(relx=0.2 + 0.16*i, rely=0.6)

for i in range(5):
    Button(root, image=photo, relief="flat", borderwidth=0).place(relx=0.2 + 0.16*i, rely=0.3)

root.mainloop()