import requests
from bs4 import BeautifulSoup
import sqlite3

# Create or connect to a SQLite database
conn = sqlite3.connect('recipes101.db')
c = conn.cursor()

# Create a table for storing recipes
c.execute('''CREATE TABLE IF NOT EXISTS recipes101
             (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, instructions TEXT, image_url TEXT)''')

def fetch_recipe_links(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Modify the selector based on the actual structure of the Taste website
    recipe_links = soup.select('h3.Title')
    return [link['href'] for link in recipe_links]

def fetch_recipe_details(recipe_url):
    response = requests.get(recipe_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Modify these selectors based on the actual structure of the Taste website
    name = soup.select_one('h1.recipe-name').get_text(strip=True)
    ingredients = '\n'.join([li.get_text(strip=True) for li in soup.select('ul.ingredients li')])
    instructions = '\n'.join([p.get_text(strip=True) for p in soup.select('div.instructions p')])
    image_url = soup.select_one('img.recipe-image')['src']
    
    return name, ingredients, instructions, image_url

def save_recipe_to_db(name, ingredients, instructions, image_url):
    c.execute("INSERT INTO recipes101 (name, ingredients, instructions, image_url) VALUES (?, ?, ?, ?)",
              (name, ingredients, instructions, image_url))
    conn.commit()

def main():
    base_url = 'https://www.taste.com.au/recipes'
    recipe_links = fetch_recipe_links(base_url)
    
    for link in recipe_links:
        name, ingredients, instructions, image_url = fetch_recipe_details(link)
        save_recipe_to_db(name, ingredients, instructions, image_url)
        print(f'Saved recipe: {name}')

if __name__ == '__main__':
    main()

# Close the database connection when done
conn.close()


