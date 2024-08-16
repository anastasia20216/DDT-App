from tkinter import *
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk
import os
#get category from pervious page
cat_value = os.getenv('cat_id', 'No recipes found')
print(f"category: {cat_value}")

# Main function to run the application
def main():
    # Create the main Tkinter window
    root = Tk()
    root.title("Recipe")
    root.geometry("1600x900")
    root.config(bg='#FAF9F6')
    nav_bar = Frame(root, bg='#F5F2EB')
    nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)

    # Define a function to switch to the search window
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
        update_button()

    #This function checks if user is logged in
    def is_logged_in():
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = cursor.execute("SELECT * FROM users WHERE active_user='yes'")
        row = cursor.fetchone()
        connection.close()
        return row is not None

    #Changes login button to profile button
    def update_button():
        if is_logged_in():
            login_btn.config(text="Profile", command=profile)
        else:
            login_btn.config(text="Login", command=login)

    def BtnClicked(obj, idx, rep_name):
        global selected_id
        selected_id = idx 
        print(idx)
        # This function gets called when a button is clicked
        print(f"recipe id {rep_id[selected_id]} recipe name: {rep_name[idx]}")
        os.environ['id'] = str(rep_id[selected_id])
        subprocess.run(["python", "recipe_pg.py"])
        root.destroy()
    
    # Establish a connection to the database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Use the selected ID from app3 to fetch the recipe details
    cat_id = (cat_value,) # Ensure it's a tuple with a single value
    print(cat_id)
    cleaned_cat_id = ", ".join(map(str, cat_id))
    query = "SELECT * FROM recipe WHERE cat=?"
    

    cursor.execute(query, cat_id) 
    rows = cursor.fetchall()  
    rep_name = [row[1] for row in rows]
    rep_id = [row[0] for row in rows]
    rep_img_paths = [row[5] for row in rows]
    connection.close()

# Load Images using PIL and ImageTk
    image_refs = []
    for img_path in rep_img_paths:
        base ='images'
        full_path = os.path.join(base, img_path)
        img = Image.open(full_path)
        img = img.resize((225,150))  #Resize
        photo = ImageTk.PhotoImage(img)
        image_refs.append(photo)

    #Frames of the top bar and side bar
    side = Frame(root, bg='#FAF9F6')
    side.place(relx=0, rely=0, relheight=1, relwidth=0.15)
    nav_bar = Frame(root, bg='#F5F2EB')
    nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)

    #Title
    label = Label(nav_bar, text='RECIPES', font=('Times', 30, 'bold'), bg='#F5F2EB')
    label.place(relx=0.8, rely=0.25)

    #Nav_bar Buttons
    Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.25)
    Button(nav_bar, text='Search', relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.13, rely=0.25)
    Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.23, rely=0.25)
    login_btn = Button(nav_bar, text="", relief="flat", borderwidth=0, command=None, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12")
    login_btn.place(relx=0.33, rely=0.25)
    update_button()
    Tilte = Label(root, text=cleaned_cat_id, font=("Helvetica", 20, "bold"), bg='#FAF9F6')
    Tilte.place(relx=0.15, rely=0.175)




    x = 0.18
    y = 0.25
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
           



    root.mainloop()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
