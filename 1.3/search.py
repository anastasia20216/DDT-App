import subprocess
import sqlite3
import re
from tkinter import *
from PIL import Image, ImageTk
import search2

def main():
    """
    Main function to run the application.
    """
    # Create the main Tkinter window
    root = Tk()
    root.title("Title")
    root.geometry("1600x900")
    root.config(bg='#FAF9F6')

    nav_bar = Frame(root, bg='#FAF9F6')
    nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

    def search():
        """
        Switch to the search window.
        """
        root.destroy()
        subprocess.run(["python", "search2.0.py"])

    def home():
        """
        Go to the home window.
        """
        root.destroy()
        subprocess.run(["python", "app3.py"])

    # Establish a connection to the database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Use the selected ID from search2 to fetch the recipe details
    rep_id = (search2.selected_id,)  # Ensure it's a tuple with a single value
    query = "SELECT id, recipe_name, ingredients, method, image FROM recipe WHERE id=?"

    try:
        cursor.execute(query, rep_id)  # Execute the query with correct parameters
        row = cursor.fetchone()  # Fetch the first matching row

        if row:  # Check if a row was found
            # Unpack the fetched data
            recipe_id, recipe_name, ingredients, method, image_data = row

            # Process the method using regex to split steps
            steps = re.split(r'(?=Step)', method)  # Split into steps based on "Step"

            # Display Recipe Name
            lbl_recipe_name = Label(
                root, text=recipe_name, font=("Helvetica", 18, "bold"), bg='#FAF9F6'
            )
            lbl_recipe_name.place(relx=0.15, rely=0.15)

            # Display Ingredients
            lbl_ingredient_header = Label(
                root, text="Ingredients", justify=LEFT, wraplength=500,
                font=("Helvetica", 14, "bold"), bg='#FAF9F6'
            )
            lbl_ingredient_header.place(relx=0.05, rely=0.25)

            lbl_ingredients = Label(
                root, text=ingredients, justify=LEFT, wraplength=500,
                bg='#FAF9F6', font=("Helvetica", 12)
            )
            lbl_ingredients.place(relx=0.05, rely=0.3)

            # Display Method
            lbl_method_header = Label(
                root, text="Method:", font=("Helvetica", 14, "bold"), bg='#FAF9F6'
            )
            lbl_method_header.place(relx=0.3, rely=0.25)

            # Method frame
            method_frame = Frame(root, bg='#FAF9F6')
            method_frame.place(relx=0.3, rely=0.2, relheight=0.6, relwidth=0.35)

            # Iterate over steps and display them
            for step in steps:
                lbl_step = Label(
                    method_frame, text=step.strip(), justify=LEFT,
                    wraplength=500, bg='#FAF9F6', font=("Helvetica", 12)
                )
                lbl_step.pack(padx=10, pady=5, side=TOP)

            # Display Image
            if image_data:
                try:
                    img = Image.open(image_data)  # Ensure correct path or method for image loading
                    img = img.resize((300, 200))  # Resize image if necessary
                    img_tk = ImageTk.PhotoImage(img)

                    lbl_image = Label(root, image=img_tk, bg='#FAF9F6')
                    lbl_image.place(relx=0.7, rely=0.2)
                except Exception as e:
                    print(f"Error loading image: {e}")
            else:
                lbl_no_image = Label(
                    root, text="No image available.", font=("Helvetica", 12),
                    bg='#FAF9F6'
                )
                lbl_no_image.place(relx=0.7, rely=0.2)
        else:
            lbl_no_recipe = Label(
                root, text="Error: No recipe found for the selected ID.",
                font=("Helvetica", 14, "bold"), bg='#FAF9F6'
            )
            lbl_no_recipe.place(relx=0.3, rely=0.2)

    except sqlite3.Error as e:
        print(f"An error occurred during database operation: {e}")

    finally:
        # Always close the cursor and connection
        cursor.close()
        connection.close()

    # Navigation bar labels and buttons
    lbl_nav_title = Label(
        nav_bar, text='Recipes', font=("Times", 30, "bold"), bg='#FAF9F6'
    )
    lbl_nav_title.place(relx=0.45, rely=0.2)

    btn_home = Button(
        nav_bar, text='Home', relief="flat", borderwidth=0, command=home,
        width=10, height=2, justify='center', bg='#FAF9F6',
        activebackground='white', font=("Times", 12)
    )
    btn_home.place(relx=0.03, rely=0.2)

    btn_recipes = Button(
        nav_bar, text='Recipes', relief="flat", borderwidth=0,
        width=10, height=2, justify='center', bg='#FAF9F6',
        activebackground='white', font=("Times", 12)
    )
    btn_recipes.place(relx=0.1, rely=0.2)

    btn_search = Button(
        nav_bar, text="Search", relief="flat", borderwidth=0, command=search,
        width=10, height=2, justify='center', bg='#FAF9F6',
        activebackground='white', font=("Times", 12)
    )
    btn_search.place(relx=0.17, rely=0.2)

    btn_favorites = Button(
        nav_bar, text="Favorites", relief="flat", borderwidth=0,
        width=10, height=2, justify='center', bg='#FAF9F6',
        activebackground='white', font=("Times", 12)
    )
    btn_favorites.place(relx=0.24, rely=0.2)

    img_logo = PhotoImage(file="profile.png").subsample(4)
    lbl_logo = Label(root, image=img_logo, bg='#FAF9F6')
    lbl_logo.place(relx=0.92, rely=0.01)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
