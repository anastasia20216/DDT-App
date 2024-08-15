from tkinter import *
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk
import os

cat_value = os.getenv('cat_id', 'No variable received')
print(f"Received id: {cat_value}")

received_id = os.getenv('id', 'No variable received')
print(f"Received id: {received_id}")
# Main function to run the application
def main():
    # Create the main Tkinter window
    root = Tk()
    root.title("Title")
    root.geometry("1600x900")
    root.config(bg='#FAF9F6')
    nav_bar = Frame(root, bg='#FAF9F6')
    nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

    # Define a function to switch to the search window
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

    def save_recipe(received_id):
        if not received_id or not received_id.isdigit():
            print("Error: Invalid ID received.")
            return

        try:
            # Connect to the SQLite database
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
        
            # SQL query to update the cell by appending new_value with a comma separator
            update_query = """
                UPDATE users 
                SET saved_rep = CASE
                    WHEN saved_rep IS NULL THEN ?
                    WHEN TRIM(saved_rep) = '' THEN ?
                    ELSE saved_rep || ', ' || ?
                END
                WHERE active_user = 'yes';
            """
        
            # Execute the query with received_id for all three placeholders
            cursor.execute(update_query, (received_id, received_id, received_id))
            connection.commit()
        
            print("Recipe saved successfully.")
    
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
        finally:
            # Ensure the connection is closed properly
            if cursor:
                cursor.close()
            if connection:
                connection.close()
     

    
    # Establish a connection to the database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Use the selected ID from app3 to fetch the recipe details
    cat_id = (cat_value,) # Ensure it's a tuple with a single value
    query = "SELECT * FROM recipe WHERE cat=?"
    

    cursor.execute(query, cat_id)  # Execute the query with correct parameters
    rows = cursor.fetchall()  # Fetch the first matching row
    rep_name = [row[1] for row in rows]
    rep_id = [row[0] for row in rows]
    # Assuming the 5th column contains image paths
    rep_img_paths = [row[5] for row in rows]
    connection.close()

# Load Images using PIL and ImageTk
    image_refs = []
    for img_path in rep_img_paths:
        img = Image.open(img_path)
        img = img.resize((225,150))  #Resize
        photo = ImageTk.PhotoImage(img)
        image_refs.append(photo)



    label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='#FAF9F6')
    label.place(relx=0.45, rely=0.2)

    Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.2)
    Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.1, rely=0.2)
    Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.17, rely=0.2)
    Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.24, rely=0.2)

    logo = PhotoImage(file="profile.png").subsample(4)
    #Label(root, image=logo, bg='#FAF9F6', command=profile).place(relx=0.92, rely=0.01)

    Tilte = Label(root, text=cat_id, font=("Helvetica", 20, "bold"), bg='#FAF9F6')
    Tilte.place(relx=0.15, rely=0.175)



    def BtnClicked(obj, idx, rep_name):
        global selected_id
        selected_id = idx 
        # This function gets called when a button is clicked
        print(f"recipe id {rep_id[selected_id]} recipe name: {rep_name[idx]}")
        os.environ['id'] = str(rep_id[selected_id])
        subprocess.run(["python", "rep_fav_feature_test.py"])
        root.destroy()
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
           


    # Start the Tkinter main loop
    root.mainloop()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
