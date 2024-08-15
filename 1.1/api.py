import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def search_recipe(api_key, query):
    api_url = "https://api.api-ninjas.com/v1/recipe"
    headers = {
        "X-Api-Key": api_key
    }
    params = {
        "query": query
    }
    response = requests.get(api_url + query, headers={'X-Api-Key': 'YOUR_API_KEY'})
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            recipe = data[0]
            return {
                "title": recipe["title"],
                "ingredients": recipe["ingredients"],
                "instructions": recipe["instructions"]
            }
        else:
            return None
    else:
        return None

def display_recipe():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search term.")
        return
    
    api_key = "nzis+ogR1PnUdYQmhmET8Q==h6JfazYyZnM1QLbN"
    recipe = search_recipe(api_key, query)
    if recipe:
        recipe_title.set(recipe["title"])
        ingredients_text.delete(1.0, tk.END)
        ingredients_text.insert(tk.END, "\n".join(recipe["ingredients"]))
        instructions_text.delete(1.0, tk.END)
        instructions_text.insert(tk.END, recipe["instructions"])
    else:
        messagebox.showerror("Error", "No recipe found. Please try again.")

# Create the main window
root = tk.Tk()
root.title("Recipe Search")

# Search input
search_label = ttk.Label(root, text="Search for a recipe:", font=("Helvetica", 12))
search_label.pack(pady=5)
search_entry = ttk.Entry(root, width=50)
search_entry.pack(pady=5)

# Search button
search_button = ttk.Button(root, text="Search", command=display_recipe)
search_button.pack(pady=10)

# Recipe title
recipe_title = tk.StringVar()
title_label = ttk.Label(root, textvariable=recipe_title, font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Ingredients label and text box
ingredients_label = ttk.Label(root, text="Ingredients:", font=("Helvetica", 12, "bold"))
ingredients_label.pack(pady=5)
ingredients_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
ingredients_text.pack(pady=5)

# Instructions label and text box
instructions_label = ttk.Label(root, text="Instructions:", font=("Helvetica", 12, "bold"))
instructions_label.pack(pady=5)
instructions_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
instructions_text.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

