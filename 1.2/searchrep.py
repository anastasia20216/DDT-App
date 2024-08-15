from tkinter import *
import subprocess
import sqlite3
import re
from PIL import Image, ImageTk
import os

selected_id = os.getenv('ids', 'No variable received')
print(f"Received id: {selected_id}")


# Main function to run the application
def main():
    # Create the main Tkinter window
    root = Tk()
    root.title("Title")
    root.geometry("1600x900")
    root.config(bg='#FAF9F6')
    nav_bar = Frame(root, bg='#FAF9F6')
    nav_bar.place(relx=0, rely=0, relheight=0.08, relwidth=1)

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

    def save_recipe(selected_id):
        if not selected_id or not selected_id.isdigit():
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
            cursor.execute(update_query, (selected_id, selected_id, selected_id))
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
            ingredient.place(relx=0.05, rely=0.2)
            lbl_ingredients = Label(root, text=f"{ingredients}", justify=LEFT, wraplength=500, bg='#FAF9F6', font=("Helvetica", 12))
            lbl_ingredients.place(relx=0.05, rely=0.3)
            
            # Display Method
            lbl_method = Label(root, text="Method:", font=("Helvetica", 14, "bold"), bg='#FAF9F6')
            lbl_method.place(relx=0.3, rely=0.2)

            #method frame
            med_frame = Frame(root, bg='#FAF9F6')
            med_frame.pack(fill='both', expand=True, padx=450, pady=200)


            # Iterate over steps and display them
            for i in range(len(steps)):
                lbl_step = Label(med_frame, text=steps[i].strip(), justify=LEFT, wraplength=500, bg='#FAF9F6', font=("Helvetica", 12))
                lbl_step.pack(padx=10, pady=5, anchor='w')
            

            
            # Display Image
            if image_data:
                # Convert image blob to ImageTk format for Tkinter display
                try:
                    img = Image.open(image_data)  # Ensure correct path or method for image loading
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

    label = Label(nav_bar, text='Recipes', font="Times 30 bold", bg='#FAF9F6')
    label.place(relx=0.45, rely=0.2)

    Button(nav_bar, text='Home', relief="flat", borderwidth=0, command=home, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.03, rely=0.2)
    Button(nav_bar, text='Recipes', relief="flat", borderwidth=0, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.1, rely=0.2)
    Button(nav_bar, text="Search", relief="flat", borderwidth=0, command=search, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.17, rely=0.2)
    Button(nav_bar, text="Favorites", relief="flat", borderwidth=0, width=10, height=2, justify='center', bg='#FAF9F6', activebackground='white', font="Times, 12").place(relx=0.24, rely=0.2)

    logo = PhotoImage(file="profile.png").subsample(4)
    Label(root, image=logo, bg='#FAF9F6').place(relx=0.92, rely=0.01)

    heart = PhotoImage(file="heart.png").subsample(5)
    save_rep = Button(root, text="Save Recipe  ", image=heart, compound=RIGHT, relief="flat", borderwidth=0, font=("Helvetica", 14) , justify='center', padx=10, pady=10, command=lambda: save_recipe(selected_id))
    save_rep.place(relx=0.7, rely=0.5)

    # Start the Tkinter main loop
    root.mainloop()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
