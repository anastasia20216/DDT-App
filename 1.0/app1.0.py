from tkinter import *


root = Tk()
root.title("Title")
root.geometry("1600x900")
root.config(bg="white")
side = Frame(root, bg='light grey')
side.place(relx=0, rely=0, relheight=1, relwidth=0.18)
nav_bar = Frame(root, bg='light grey')
nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='light grey')
label.place(relx=0.45, rely=0.2)

Button(nav_bar, text='Home').place(relx=0.03, rely=0.2)
Button(nav_bar, text='Recipes').place(relx=0.1, rely=0.2)
Button(nav_bar, text="Exit").place(relx=0.17, rely=0.2)
Button(nav_bar, text="Favorites").place(relx=0.24, rely=0.2)
Button(nav_bar, text="Search").place(relx=0.32, rely=0.2)


logo = PhotoImage(file="logo.png").zoom(3).subsample(6)
Label(root, image=logo).place(relx=0.9, rely=0.006)

Label(root, text="Search", bg="light grey").place(relx=0.03, rely=0.08)
search_bar = Entry(root)
search_bar.place(relx=0.03, rely=0.1, relheight=0.03, relwidth=0.14)

Font1 = ("Times", 16)
Label(root, text='CATEGORIES', font=Font1,  bg='light grey').place(relx=0.03, rely=0.15)

# Load image once and reuse for buttons
text1 = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item6', 'item6']
for i in range(8):
    Button(root, text=text1[i]).place(relx=0.04, rely=0.2 + 0.06*i)


Label(root, text='HEADING', font=Font1, bg='white').place(relx=0.22, rely=0.15)
photo = PhotoImage(file="download.png").zoom(25).subsample(32)
for i in range(5):
    Button(root, image=photo).place(relx=0.2 + 0.16*i, rely=0.6)

for i in range(5):
    Button(root, image=photo).place(relx=0.2 + 0.16*i, rely=0.3)

root.mainloop()