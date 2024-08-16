from tkinter import *
import tkinter as tk
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk
import os

selected_id = os.getenv('ids', 'No variable received')
print(f"Received id: {selected_id}")
key = os.getenv('keyword', 'No keyword received')
print(f"keyword: {key}")



# Main function to run the application
def main():
    # Create the main Tkinter window
    root = Tk()
    root.title("Recipe")
    root.geometry("1600x900")
    root.config(bg='#FAF9F6')
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
            save_rep.config(text='Save Recipe')
            unsave_rep.config(text="Unsave Recipe")
        else:
            login_btn.config(text="Login", command=login)
            save_rep.config(text="Login to save")
            unsave_rep.config(text="Login to save")

    def go_back_to_search():
        if key is not None:
                # Create a new search window with previous search query and results
            root.destroy()
            # Assuming search2.py handles search display
            subprocess.run(["python", "search2.py", key])
        else:
            print("No previous search context found.")

    def check_if_saved(rep_id):
        # If rep_id is a tuple, unpack it
        if isinstance(rep_id, tuple):
            rep_id = rep_id[0]

        print(rep_id)
        if not rep_id or not str(rep_id).isdigit():
            print("Error: Invalid ID received.")
            return

        try:
            # Connect to the SQLite database
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            # Check if the recipe is already saved
            cursor.execute("SELECT saved_rep FROM users WHERE active_user = 'yes';")
            saved_reps = cursor.fetchone()
                    # Handle case where no recipes are saved (saved_reps is None)
            if saved_reps is None or saved_reps[0] is None:
                saved_reps_list = []
            else:
                saved_reps_list = saved_reps[0].split(', ')
            if rep_id in saved_reps_list:
                print("Recipe is already saved.")
                unsave_rep.config(state=tk.NORMAL)
                unsave_rep.tkraise()
                save_rep.config(state=tk.DISABLED)
                return   
        except sqlite3.Error as e:
            print(f"Database error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def save_recipe(rep_id):
        # If rep_id is a tuple, unpack it
        if isinstance(rep_id, tuple):
            rep_id = rep_id[0]

        print(rep_id)
        if not rep_id or not str(rep_id).isdigit():
            print("Error: Invalid ID received.")
            return

        try:
            # Connect to the SQLite database
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            # Check if the recipe is already saved
            cursor.execute("SELECT saved_rep FROM users WHERE active_user = 'yes';")
            saved_reps = cursor.fetchone()
                                            # Handle case where no recipes are saved (saved_reps is None)
            if saved_reps is None or saved_reps[0] is None:
                saved_reps_list = []
            else:
                saved_reps_list = saved_reps[0].split(', ')
            if rep_id in saved_reps_list:
                print("Recipe is already saved.")
                unsave_rep.config(state=tk.NORMAL)
                unsave_rep.tkraise()
                save_rep.config(state=tk.DISABLED)
                return
            else:
                unsave_rep.config(state=tk.DISABLED)
                save_rep.config(state=tk.NORMAL)
                save_rep.tkraise()

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
            cursor.execute(update_query, (rep_id, rep_id, rep_id))
            connection.commit()
        
            print("Recipe saved successfully.")
            save_rep.config(text='Recipe Saved')
            unsave_rep.config(state=tk.NORMAL)
            unsave_rep.tkraise()

        except sqlite3.Error as e:
            print(f"Database error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def unsave_recipe(rep_id):
        # If rep_id is a tuple, unpack it
        if isinstance(rep_id, tuple):
            rep_id = rep_id[0]

        print(f"Unsaving recipe {rep_id}")
        if not rep_id or not str(rep_id).isdigit():
            print("Error: Invalid ID received.")
            return

        try:
            # Connect to the SQLite database
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            # Get the current saved recipes
            cursor.execute("SELECT saved_rep FROM users WHERE active_user = 'yes';")
            saved_reps = cursor.fetchone()
        
            if saved_reps:
                saved_reps_list = saved_reps[0].split(', ')
                if rep_id in saved_reps_list:
                    # Remove the recipe ID
                    saved_reps_list.remove(rep_id)
                    updated_reps = ', '.join(saved_reps_list)
                
                    # Update the database with the new list
                    cursor.execute("UPDATE users SET saved_rep = ? WHERE active_user = 'yes';", (updated_reps,))
                    connection.commit()
                
                    print("Recipe unsaved successfully.")
                    unsave_rep.config(state=tk.DISABLED)
                    save_rep.config(state=tk.NORMAL)
                    save_rep.config(text='Save Recipe')
                    save_rep.tkraise()
                else:
                    print("Recipe ID not found in saved list.")
            else:
                print("No saved recipes found.")

        except sqlite3.Error as e:
            print(f"Database error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
     

    # Establish a connection to the database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Use the selected ID from app3 to fetch the recipe details
    rep_id = (selected_id,) # Ensure it's a tuple with a single value
    query = "SELECT id, recipe_name, ingridents, method, image FROM recipe WHERE id=?"
    
    try:
        cursor.execute(query, rep_id)  # Execute the query with correct parameters
        row = cursor.fetchone()  # Fetch the first matching row

        if row:  # Check if a row was found
            # Unpack the fetched data
            recipe_id, recipe_name, ingredients, method, image_data = row
            
            # Process the method using regex to split steps
            steps = re.split(r'(?=Step)', method)  # Split into steps based on "Step"
            
            # Display Recipe Name
            lbl_recipe_name = Label(root, text=recipe_name, font=("Helvetica", 18, "bold"), bg='#FAF9F6')
            lbl_recipe_name.place(relx=0.15, rely=0.12)
            
            # Display Ingredients
            ingredient = Label(root, text="Ingredients", justify=LEFT, wraplength=500, font=("Helvetica", 14, "bold"), bg='#FAF9F6')
            ingredient.place(relx=0.05, rely=0.22)
            lbl_ingredients = Label(root, text=f"{ingredients}", justify=LEFT, wraplength=500, bg='#FAF9F6', font=("Helvetica", 12))
            lbl_ingredients.place(relx=0.05, rely=0.3)
            
           

            #method frame
            med_frame = Frame(root, bg='#FAF9F6')
            med_frame.pack(fill='both', expand=True, padx=450, pady=200)

             # Display Method
            lbl_method = Label(root, text="Method:", font=("Helvetica", 14, "bold"), bg='#FAF9F6')
            lbl_method.place(relx=0.3, rely=0.22)


            # Iterate over steps and display them
            for i in range(len(steps)):
                lbl_step = Label(med_frame, text=steps[i].strip(), justify=LEFT, wraplength=500, bg='#FAF9F6', font=("Helvetica", 12))
                lbl_step.pack(padx=10, pady=5, anchor='w')
            

            
            # Display Image
            if image_data:
                # Convert image blob to ImageTk format for Tkinter display
                try:
                    base ='images'
                    full_path = os.path.join(base, image_data)
                    img = Image.open(full_path)  # Ensure correct path or method for image loading
                    img = img.resize((300, 200))  # Resize image if necessary
                    img_tk = ImageTk.PhotoImage(img)
                    
                    lbl_image = Label(root, image=img_tk, bg='#FAF9F6')
                    lbl_image.place(relx=0.7, rely=0.2)
                except Exception as e:
                    print(f"Error loading image: {e}")


        else:
            # No recipe found
            lbl_no_recipe = Label(root, text="Error: No recipe found for the selected ID.", font=("Helvetica", 14, "bold"), bg='#FAF9F6')
            lbl_no_recipe.place(relx=0.3, rely=0.2)
    
    except sqlite3.Error as e:
        print(f"An error occurred during database operation: {e}")
    
    finally:
        # Always close the cursor and connection
        cursor.close()
        connection.close()

    nav_bar = Frame(root, bg='#F5F2EB')
    nav_bar.place(relx=0, rely=0, relheight=0.11, relwidth=1)
    #Title
    label = Label(nav_bar, text='RECIPES', font=('Times', 30, 'bold'), bg='#F5F2EB')
    label.place(relx=0.8, rely=0.25)

    #Nav_bar Buttons
    Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.25)
    Button(nav_bar, text='Search', relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.13, rely=0.25)
    Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, command=show_fav, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.23, rely=0.25)
    Button(nav_bar, text="Profile", relief="flat", borderwidth=0, command=profile, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.33, rely=0.25)
    login_btn = Button(nav_bar, text="", relief="flat", borderwidth=0, command=None, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12")
    login_btn.place(relx=0.33, rely=0.25)
    

    heart = PhotoImage(file="images/heart.png").subsample(5)

    #the unsave button (initially disabled)
    unsave_rep = tk.Button(root, text='Unsave Recipe', command=lambda: unsave_recipe(rep_id), state=tk.DISABLED, relief="flat", borderwidth=0, font=("Helvetica", 14) , justify='center', padx=20, pady=10) 
    unsave_rep.place(relx=0.7, rely=0.5)
    save_rep = Button(root, text="Save Recipe ", image=heart, compound=RIGHT, relief="flat", borderwidth=0, font=("Helvetica", 14) , justify='center', padx=10, pady=10, command=lambda: save_recipe(rep_id))
    save_rep.place(relx=0.7, rely=0.5)
    arrow = PhotoImage(file="images/arrow.png")
    return_button = Button(root, text="Search Results", image=arrow, compound=LEFT, command=go_back_to_search, font=("Helvetica", 10), bg='#FAF9F6', relief="flat")
    return_button.place(relx=0.02, rely=0.12)
    check_if_saved(rep_id)
    update_button()
    # Start the Tkinter main loop
    root.mainloop()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
